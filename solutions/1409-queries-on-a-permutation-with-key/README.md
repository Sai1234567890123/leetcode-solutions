# 1409. Queries on a Permutation With Key

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/queries-on-a-permutation-with-key/](https://leetcode.com/problems/queries-on-a-permutation-with-key/)  
**Topics:** Array, Binary Indexed Tree, Simulation, Sqrt Decomposition

---

## 📝 Problem Statement

Given the array `queries` of positive integers between `1` and `m`, you have to process all `queries[i]` (from `i=0` to `i=queries.length-1`) according to the following rules:

	- In the beginning, you have the permutation `P=[1,2,3,...,m]`.

	- For the current `i`, find the position of `queries[i]` in the permutation `P` (**indexing from 0**) and then move this at the beginning of the permutation `P`. Notice that the position of `queries[i]` in `P` is the result for `queries[i]`.

Return an array containing the result for the given `queries`.

 
Example 1:

```

**Input:** queries = [3,1,2,1], m = 5
**Output:** [2,1,2,1] 
**Explanation:** The queries are processed as follow: 
For i=0: queries[i]=3, P=[1,2,3,4,5], position of 3 in P is **2**, then we move 3 to the beginning of P resulting in P=[3,1,2,4,5]. 
For i=1: queries[i]=1, P=[3,1,2,4,5], position of 1 in P is **1**, then we move 1 to the beginning of P resulting in P=[1,3,2,4,5]. 
For i=2: queries[i]=2, P=[1,3,2,4,5], position of 2 in P is **2**, then we move 2 to the beginning of P resulting in P=[2,1,3,4,5]. 
For i=3: queries[i]=1, P=[2,1,3,4,5], position of 1 in P is **1**, then we move 1 to the beginning of P resulting in P=[1,2,3,4,5]. 
Therefore, the array containing the result is [2,1,2,1].  

```

Example 2:

```

**Input:** queries = [4,1,2,2], m = 4
**Output:** [3,1,2,0]

```

Example 3:

```

**Input:** queries = [7,5,5,8,3], m = 8
**Output:** [6,5,0,7,5]

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class FenwickTree:
    """Binary Indexed Tree (Fenwick Tree) supporting point updates and prefix sum queries."""
    __slots__ = ('tree', 'size')

    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index: int, delta: int) -> None:
        """Adds delta to the element at the given 1-based index."""
        while index <= self.size:
            self.tree[index] += delta
            index += index & (-index)

    def query(self, index: int) -> int:
        """Returns the prefix sum from 1 to index (inclusive)."""
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & (-index)
        return total


class Solution:
    def processQueries(self, queries: list[int], m: int) -> list[int]:
        """
        Processes queries using a Fenwick Tree (Binary Indexed Tree).
        
        Time Complexity: O((m + q) * log(m + q)) where q = len(queries)
        Space Complexity: O(m + q)
        """
        n = len(queries)
        total_size = m + n
        bit = FenwickTree(total_size)
        
        # pos[val] stores the 1-based position of 'val' in the underlying array
        pos = [0] * (m + 1)
        
        # Elements 1 to m are initially placed at indices (n + 1) to (n + m)
        # This leaves n empty slots (1 to n) for moving elements to the front.
        for val in range(1, m + 1):
            curr_pos = n + val
            pos[val] = curr_pos
            bit.update(curr_pos, 1)
            
        result = []
        # curr_front tracks the next available slot for an element moved to the front
        curr_front = n
        
        for q in queries:
            curr_idx = pos[q]
            # The 0-based index in the current permutation is the count of elements
            # strictly before curr_idx.
            result.append(bit.query(curr_idx - 1))
            
            # Remove element from its current position
            bit.update(curr_idx, -1)
            
            # Place element at the new front
            bit.update(curr_front, 1)
            pos[q] = curr_front
            
            curr_front -= 1
            
        return result
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

A naive simulation using a dynamic array (like Python's `list.index()` and `list.insert(0, ...)`) takes $O(m)$ per query. With $q$ queries, the naive approach takes $O(q \cdot m)$ time. While $m, q \le 1000$ in this specific LeetCode problem, in real-world scenarios or large-scale interviews, $m$ and $q$ can be up to $10^5$ or $10^6$, where an $O(q \cdot m)$ solution will result in Time Limit Exceeded (TLE).

To optimize this to $O(q \log(m + q))$:
1. Moving an element to the front of an array shifts all preceding elements. Instead of shifting, we can allocate a virtual array of size $m + q$.
2. The initial $m$ elements can be placed in positions $[q + 1, q + 2, \dots, q + m]$.
3. Positions $[1, q]$ are left open for prepending operations. Every time an element is moved to the front, it occupies the next unused position to the left (i.e., position $q, q - 1, \dots, 1$).
4. The 0-indexed position of an element $x$ in the current permutation corresponds to the number of active elements strictly to the left of $x$'s position.
5. A **Fenwick Tree (Binary Indexed Tree)** can efficiently maintain the count of active elements in $O(\log(m + q))$ time for both prefix sum queries and point updates.

---

### Step-by-Step Approach

1. **Size Allocation**: Allocate space for $m + q$ slots.
2. **Initial Placement**:
   - For each number $x \in [1, m]$, place it at index $n + x$ (1-based index).
   - Set the count at index $n + x$ in the Fenwick Tree to $1$.
   - Maintain a direct lookup array `pos[x] = n + x`.
3. **Query Processing**:
   - For each query $q$:
     - Look up its position `curr_idx = pos[q]`.
     - Count active elements before `curr_idx` using `bit.query(curr_idx - 1)`. Append this to `result`.
     - Deactivate the old position: `bit.update(curr_idx, -1)`.
     - Move $q$ to `curr_front`: `bit.update(curr_front, 1)` and `pos[q] = curr_front`.
     - Decrement `curr_front`.

---

### Complexity Analysis

- **Time Complexity**:
  - **Initialization**: $O(m \log(m + n))$ to insert $m$ elements into the BIT.
  - **Per Query**: $O(\log(m + n))$ for one prefix sum query and two point updates.
  - **Total Time**: $O((m + n) \log(m + n))$ where $n = \text{len}(queries)$. This easily scales to $10^5$ constraints.
- **Space Complexity**:
  - Fenwick Tree array: $O(m + n)$.
  - Position map `pos`: $O(m)$.
  - Output array: $O(n)$.
  - **Total Auxiliary Space**: $O(m + n)$.

---

### Common Pitfalls / Mistakes

1. **1-Based vs. 0-Based Indexing**:
   - Fenwick Trees naturally operate on 1-based indexing.
   - The question requires 0-based index results. Querying `bit.query(curr_idx - 1)` directly yields the count of elements strictly before `curr_idx`, which accurately matches 0-based indexing.
2. **Off-by-one with Virtual Head**:
   - Pre-allocating fewer than $q$ slots in front will cause index out-of-bounds if all queries prepend distinct elements. $n$ free prefix slots are necessary and sufficient.
3. **Re-insertion Redundancy**:
   - If the element queried is already at index 0 (i.e. queried consecutively), simply moving it to the new `curr_front` works identically without special branching, keeping code clean.

---

### Real Interview Follow-Up Questions

1. **What if queries are streaming indefinitely ($q \to \infty$) and memory is constrained?**
   - *Answer*: If $q \gg m$, allocating $m + q$ statically is impossible. We can:
     - Use a balanced self-balancing order-statistic tree (e.g., Red-Black Tree, Treap, or Splay Tree) where each node tracks subtree sizes. Rotations and deletion/re-insertion to head take $O(\log m)$ time and only $O(m)$ space.
     - Alternatively, periodic re-indexing/compaction of the Fenwick Tree: when the left buffer fills up, rebuild the Fenwick Tree in $O(m \log m)$ every $O(m)$ operations, yielding amortized $O(\log m)$ time and $O(m)$ space.

2. **How to handle concurrency if queries are read/write from multiple threads?**
   - *Answer*: Since queries modify the structure sequentially (order-dependent), strict sequential consistency is required. However, we could batch queries and compute permutation cycles, or use read-write locks / lock-free skip lists with subtree sizing if read queries only inspected positions without mutations.
