# 0535. Encode and Decode TinyURL

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/encode-and-decode-tinyurl/](https://leetcode.com/problems/encode-and-decode-tinyurl/)  
**Topics:** Hash Table, String, Design, Hash Function

---

## 📝 Problem Statement

Note: This is a companion problem to the System Design problem: Design TinyURL.

TinyURL is a URL shortening service where you enter a URL such as `https://leetcode.com/problems/design-tinyurl` and it returns a short URL such as `http://tinyurl.com/4e9iAk`. Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Implement the `Solution` class:

	- `Solution()` Initializes the object of the system.

	- `String encode(String longUrl)` Returns a tiny URL for the given `longUrl`.

	- `String decode(String shortUrl)` Returns the original long URL for the given `shortUrl`. It is guaranteed that the given `shortUrl` was encoded by the same object.

 
Example 1:

```

**Input:** url = "https://leetcode.com/problems/design-tinyurl"
**Output:** "https://leetcode.com/problems/design-tinyurl"

**Explanation:**
Solution obj = new Solution();
string tiny = obj.encode(url); // returns the encoded tiny url.
string ans = obj.decode(tiny); // returns the original url after decoding it.

```

 
**Constraints:**

	- `1 4`

	- `url` is guranteed to be a valid URL.

---

## 💻 Implementation (python3)

```py
import random
import string

class Codec:
    def __init__(self):
        # Character set for Base62 encoding: 26 lowercase + 26 uppercase + 10 digits = 62 characters
        self.chars = string.ascii_letters + string.digits
        self.code_length = 6
        self.base_url = "http://tinyurl.com/"
        
        # Bi-directional mapping to ensure idempotence and fast lookups
        self.url_to_code = {}
        self.code_to_url = {}

    def _generate_code(self) -> str:
        """Generates a random 6-character Base62 alphanumeric string."""
        return ''.join(random.choices(self.chars, k=self.code_length))

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        # If the URL is already shortened, return the existing tiny URL (idempotency)
        if longUrl in self.url_to_code:
            return self.base_url + self.url_to_code[longUrl]
        
        # Generate a unique 6-character code, handling collisions
        code = self._generate_code()
        while code in self.code_to_url:
            code = self._generate_code()
            
        # Store bi-directional mappings
        self.code_to_url[code] = longUrl
        self.url_to_code[longUrl] = code
        
        return self.base_url + code

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        # Extract the 6-character key from the end of the URL
        code = shortUrl.replace(self.base_url, "")
        return self.code_to_url.get(code, "")

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

LeetCode 535 is a bridge between algorithmic problem solving and low-level system design. 

In a production URL shortener, we want:
1. **Short URL Length**: Keeping URLs as short as possible.
2. **Low Collision Probability**: Large address space.
3. **Non-predictability**: Sequential IDs (1, 2, 3...) allow adversaries to scrape the entire database by simply incrementing IDs.
4. **Idempotence**: Encoding the same URL multiple times should ideally return the existing shortened URL to save storage.

By using Base62 encoding (a-z, A-Z, 0-9), a 6-character string provides:
$$62^6 \approx 56.8 \text{ billion unique URLs}$$
This is more than sufficient for high-volume requirements. We maintain two hash maps:
- `url_to_code`: Maps `longUrl -> code` (ensures idempotency).
- `code_to_url`: Maps `code -> longUrl` (provides $O(1)$ decoding).

---

### Step-by-Step Approach

1. **Initialization**: Define the alphabet (Base62) and instantiate two hash maps (`url_to_code` and `code_to_url`).
2. **Encode**:
   - Check if `longUrl` already exists in `url_to_code`. If so, return the cached result.
   - Generate a random 6-character string from the Base62 character pool.
   - Loop until a non-colliding key is generated.
   - Store the key in both mappings and return `http://tinyurl.com/` concatenated with the key.
3. **Decode**:
   - Strip the prefix `http://tinyurl.com/` to retrieve the 6-character code.
   - Look up the code in `code_to_url` and return the original URL.

---

### Complexity Analysis

- **Time Complexity**:
  - `encode`: $\mathcal{O}(L)$ on average, where $L$ is the length of `longUrl` (due to hashing the string). The 6-character random generation and collision check takes $\mathcal{O}(1)$ expected time since the collision rate is negligible with $56.8 \times 10^9$ possibilities.
  - `decode`: $\mathcal{O}(K)$ where $K$ is the length of `shortUrl`, which is bounded by a small constant ($\approx 26$ characters). Thus, it runs in $\mathcal{O}(1)$ time.

- **Space Complexity**:
  - $\mathcal{O}(N \cdot L)$ where $N$ is the total number of unique URLs encoded and $L$ is the average length of the original URLs, stored in both hash maps.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Sequential / Incremental Counters**: Using a simple incrementing counter (`http://tinyurl.com/1`, `http://tinyurl.com/2`) makes the service vulnerable to enumeration attacks (crawlers easily scrape all data).
2. **Using Standard Hash Functions Directly**: Using MD5 or SHA-256 generates strings that are 32 or 64 hex characters long, which defeats the purpose of "shortening" the URL. Truncating standard hashes still requires collision handling.
3. **No Bi-directional Mapping**: Storing only `code -> url` means encoding the same long URL 1,000 times wastes 1,000 keys and storage slots.
4. **Hardcoding String Slicing**: Using `shortUrl[-6:]` breaks if someone supplies a custom alias or the code length changes. Stripping the base URL or using `rsplit('/', 1)` is more robust.

---

### Real Interview Follow-Up Questions & System Design Considerations

1. **How do you handle massive scale / distributed generation?**
   - *Answer*: In a distributed system, a single counter or local random generator faces collision or coordination overhead. We can use a distributed ID generator (e.g., Twitter Snowflake) or a distributed counter service (e.g., ZooKeeper/etcd allocating ID ranges like `[1M, 2M)` to specific worker nodes) combined with Base62 conversion.

2. **How to handle concurrency and race conditions?**
   - *Answer*: When multiple threads/nodes try to encode the same URL simultaneously, we rely on database uniqueness constraints (e.g., unique index on `long_url` and `short_code`) with `INSERT ... ON CONFLICT DO NOTHING` / transactions.

3. **How do you implement URL expiration (TTL)?**
   - *Answer*: Store an `expires_at` timestamp. Use Redis with TTL for caching hot URLs and a lazy deletion or periodic batch job on the primary database (e.g., Cassandra / PostgreSQL) to prune expired rows.

4. **How would you support custom aliases (e.g., `tinyurl.com/my-custom-link`)?**
   - *Answer*: Allow an optional `custom_alias` parameter. If provided, check if it's already reserved in the database. If taken, throw a `409 Conflict`; otherwise, assign it directly.
