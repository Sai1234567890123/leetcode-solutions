# Distributed LSM-Tree & Write-Ahead Log Storage Engine
**Model:** `gemini-3.8-flash` on Google Cloud Vertex AI
**GCP Project:** `aiautomationplatform`
**Executed At:** `2026-10-05T07:54:24.856041+00:00`
**Latency:** `31.13s` | **Tokens:** `4260` (Prompt: `168`, Output: `2878`)

---

# PRODUCTION STORAGE ENGINE ARCHITECTURE

```
+---------------------------------------------------------------------------------------------------+
|                                      CLIENT WRITE PIPELINE                                        |
+---------------------------------------------------------------------------------------------------+
           |                                                                   |
           v (Zero-Copy Append)                                                v (Concurrent Insert)
+------------------------------------+                             +--------------------------------+
|    MEM-MAPPED WAL RING BUFFER      |                             | LOCK-FREE SKIPLIST (MEMTABLE)  |
|  - Atomic LSN Reservation Ticket   |                             |  - CAS Next Pointers           |
|  - Cacheline Aligned Mutex Array   |                             |  - Relaxed Multi-Tower Reads   |
|  - Microsecond Group Coalescing    |                             |  - Zero-Alloc Arena Allocation |
+------------------------------------+                             +--------------------------------+
           |                                                                   |
           | (fdatasync thread pool)                                           | (Frozen when size >= 64MB)
           v                                                                   v
+------------------------------------+                             +--------------------------------+
|       PERSISTENT DISK LOG          |                             |       IMMUTABLE MEMTABLE       |
+------------------------------------+                             +--------------------------------+
                                                                               |
                                                                               | (Background Flush)
                                                                               v
+---------------------------------------------------------------------------------------------------+
|                                  LEVELED STORAGE ENGINE (L0 - Ln)                                 |
+---------------------------------------------------------------------------------------------------+
|  L0: [SSTable 0_1] [SSTable 0_2] [SSTable 0_3]  <-- Key ranges overlap (Requires multi-way merge)|
+---------------------------------------------------------------------------------------------------+
|  L1: [  SSTable 1_1  ] [  SSTable 1_2  ] [  SSTable 1_3  ] <-- Disjoint keys (Max Size: 256 MB)    |
+---------------------------------------------------------------------------------------------------+
|  L2: [      SSTable 2_1      ] [      SSTable 2_2      ]   <-- Disjoint keys (Max Size: 2.56 GB)  |
+---------------------------------------------------------------------------------------------------+
                                         |
                                         v
+---------------------------------------------------------------------------------------------------+
|                                   SSTABLE BINARY SPECIFICATION                                    |
+---------------------------------------------------------------------------------------------------+
| Data Block 0 | ... | Data Block N | Block Index Block | Filter Block (Blocked Bloom) | 48B Footer |
+---------------------------------------------------------------------------------------------------+
```

---

# 1. Zero-Copy WAL Architecture & Implementation

### Storage Architecture
The Write-Ahead Log (WAL) allocates fixed contiguous extents using `posix_fallocate()` to avoid runtime filesystem metadata allocation panics. Updates are mediated via a circular memory-mapped ring buffer with cacheline-padded atomic sequencers.

*   **Atomic Reservation**: Threads reserve unique logical offsets via `fetch_add` on an aligned monotonically increasing sequence number (LSN).
*   **Zero-Copy Serialization**: Worker threads serialize mutations directly into the mapped pointer slice yielded by their reservation ticket without intermediate userspace buffering.
*   **Group-Commit Engine**: Commits coalesce through a single-waiter, multi-producer epoch sync barrier. Threads update an atomic `ready_lsn`, while a dedicated background flushing daemon calls `fdatasync()` across dynamic range batches, minimizing IOPS overhead while guaranteeing ACID compliance.

```
Ring Buffer Memory Layout:
[ Header: Magic(8B) | LSN(8B) | Length(4B) | CRC32C(4B) | Payload (Variable) | Padding ]
^                                                        ^
|-- Cacheline-aligned (64B)                              |-- Direct pointer to MMap region
```

### Complete Implementation (`wal.hpp`)

```cpp
#pragma once

#include <atomic>
#include <cstdint>
#include <cstring>
#include <string_view>
#include <span>
#include <stdexcept>
#include <system_error>
#include <fcntl.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <immintrin.h>

class ZeroCopyWAL {
public:
    #pragma pack(push, 1)
    struct RecordHeader {
        uint64_t magic;
        uint64_t lsn;
        uint32_t length;
        uint32_t crc32c;
    };
    #pragma pack(pop)

    static constexpr uint64_t WAL_MAGIC = 0x5452414E534C4F47ULL; // "TRANSLOG"
    static constexpr size_t CACHELINE_SIZE = 64;

    explicit ZeroCopyWAL(const std::string& path, size_t capacity) 
        : capacity_(capacity), mask_(capacity - 1) {
        if ((capacity & mask_) != 0) {
            throw std::invalid_argument("Capacity must be a power of two.");
        }

        fd_ = ::open(path.c_str(), O_RDWR | O_CREAT | O_TRUNC, 0644);
        if (fd_ < 0) throw std::system_error(errno, std::generic_category());

        if (::posix_fallocate(fd_, 0, capacity_) != 0) {
            ::close(fd_);
            throw std::system_error(errno, std::generic_category());
        }

        void* addr = ::mmap(nullptr, capacity_, PROT_READ | PROT_WRITE, MAP_SHARED, fd_, 0);
        if (addr == MAP_FAILED) {
            ::close(fd_);
            throw std::system_error(errno, std::generic_category());
        }
        buffer_ = static_cast<uint8_t*>(addr);
    }

    ~ZeroCopyWAL() {
        Sync(write_lsn_.load(std::memory_order_relaxed));
        ::munmap(buffer_, capacity_);
        ::close(fd_);
    }

    uint64_t Append(uint32_t type, std::span<const uint8_t> payload) {
        const uint32_t total_size = sizeof(RecordHeader) + payload.size();
        const uint32_t aligned_size = (total_size + CACHELINE_SIZE - 1) & ~(CACHELINE_SIZE - 1);

        // Atomic multi-producer reservation ticket
        uint64_t offset = write_offset_.fetch_add(aligned_size, std::memory_order_acq_rel);
        uint64_t lsn = current_lsn_.fetch_add(1, std::memory_order_relaxed);

        if (offset + aligned_size > capacity_) {
            throw std::runtime_error("WAL Ring Buffer exhausted: capacity breached.");
        }

        uint8_t* dest = buffer_ + (offset & mask_);
        RecordHeader header{
            .magic = WAL_MAGIC,
            .lsn = lsn,
            .length = static_cast<uint32_t>(payload.size()),
            .crc32c = 0
        };

        // Hardware-accelerated CRC32C over the record payload
        uint32_t crc = 0xFFFFFFFF;
        for (size_t i = 0; i < payload.size(); ++i) {
            crc = _mm_crc32_u8(crc, payload[i]);
        }
        header.crc32c = crc ^ 0xFFFFFFFF;

        std::memcpy(dest, &header, sizeof(RecordHeader));
        std::memcpy(dest + sizeof(RecordHeader), payload.data(), payload.size());

        // Notify sync pipeline of updated sequential continuous range
        uint64_t expected = lsn;
        while (!write_lsn_.compare_exchange_weak(expected, lsn + 1, 
                                                std::memory_order_release, 
                                                std::memory_order_relaxed)) {
            _mm_pause();
            expected = lsn;
        }

        return lsn;
    }

    void Sync(uint64_t target_lsn) {
        uint64_t synced = synced_lsn_.load(std::memory_order_acquire);
        while (synced < target_lsn) {
            if (sync_mutex_.exchange(true, std::memory_order_acquire)) {
                // Secondary waiters yield to reduce cache bus thrashing
                _mm_pause();
                synced = synced_lsn_.load(std::memory_order_acquire);
                continue;
            }

            // Double check inside the synchronization lock
            synced = synced_lsn_.load(std::memory_order_relaxed);
            uint64_t current_w = write_lsn_.load(std::memory_order_acquire);
            if (synced < current_w) {
                ::fdatasync(fd_);
                synced_lsn_.store(current_w, std::memory_order_release);
            }

            sync_mutex_.store(false, std::memory_order_release);
            break;
        }
    }

    [[nodiscard]] uint8_t* Data() const noexcept { return buffer_; }
    [[nodiscard]] size_t Capacity() const noexcept { return capacity_; }

private:
    int fd_;
    const size_t capacity_;
    const size_t mask_;
    uint8_t* buffer_;

    alignas(CACHELINE_SIZE) std::atomic<uint64_t> write_offset_{0};
    alignas(CACHELINE_SIZE) std::atomic<uint64_t> current_lsn_{1};
    alignas(CACHELINE_SIZE) std::atomic<uint64_t> write_lsn_{1};
    alignas(CACHELINE_SIZE) std::atomic<uint64_t> synced_lsn_{0};
    alignas(CACHELINE_SIZE) std::atomic<bool> sync_mutex_{false};
};
```

---

# 2. Lock-Free Concurrent SkipList (MemTable)

### Structural Mechanics & Invariants
The MemTable provides atomic linearizable inserts, concurrent lock-free point lookups, and monotonic scans without requiring coarse-grained synchronization locks.

*   **Atomic Pointer Tagging**: Deletion and link modification use single-word atomic operations (`std::atomic<Node*>`). Node towers are updated layer-by-layer from bottom to top via `compare_exchange_strong`.
*   **No Allocation Locks**: Tower height allocation uses an atomic, thread-local splitmix64 uniform random generator, bounded to a maximum height $K = 32$.
*   **Search Optimizations**: Search steps advance via relaxed-order memory dereferences across higher levels, followed by acquire fences when dropping to level 0, ensuring consistent view transitions across cache domains without global stops.

```
SkipList Layout:
Level 3: [Head] ------------------------------> [Node 12] ---------------------> nullptr
Level 2: [Head] -------------> [Node 5] --------> [Node 12] ---------> [Node 25] -> nullptr
Level 1: [Head] -> [Node 3] -> [Node 5] -> [N8]-> [Node 12] -> [N17]-> [Node 25] -> nullptr
Level 0: [Head] -> [Node 3] -> [Node 5] -> [N8]-> [Node 12] -> [N17]-> [Node 25] -> nullptr
```

### Complete Implementation (`skiplist.hpp`)

```cpp
#pragma once

#include <atomic>
#include <cstdint>
#include <cstring>
#include <string_view>
#include <array>
#include <new>

template <typename KeyComparator>
class ConcurrentSkipList {
public:
    static constexpr int MAX_HEIGHT = 32;
    static constexpr uint32_t BRANCHING_PROBABILITY_RECIPROCAL = 4; // p = 0.25

    struct Node {
        std::string_view key;
        std::string_view value;
        uint64_t lsn;
        int height;
        std::atomic<Node*> forward[1];

        static Node* Create(std::string_view k, std::string_view v, uint64_t seq, int h) {
            size_