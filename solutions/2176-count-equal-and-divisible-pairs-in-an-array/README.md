# 2176. Count Equal and Divisible Pairs in an Array

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/](https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/)  
**Topics:** Array

---

## 📝 Problem Statement

Given a **0-indexed** integer array `nums` of length `n` and an integer `k`, return *the **number of pairs*** `(i, j)` *where* `0  
Example 1:

```

**Input:** nums = [3,1,2,2,2,1,3], k = 2
**Output:** 4
**Explanation:**
There are 4 pairs that meet all the requirements:
- nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
- nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
- nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
- nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.

```

Example 2:

```

**Input:** nums = [1,2,3,4], k = 1
**Output:** 0
**Explanation:** Since no value in nums is repeated, there are no pairs (i,j) that meet all the requirements.

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
from collections import defaultdict
from math import gcd

class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        """
        Counts pairs (i, j) with 0 <= i < j < n such that:
        nums[i] == nums[j] and (i * j) % k == 0.

        Optimized approach:
        Group indices by their value. For each value, track the frequency
        of gcd(i, k) seen so far. An index j pairs with any previous index i
        if (gcd(i, k) * gcd(j, k)) % k == 0.
        """
        # Group indices by their corresponding value in nums
        val_to_indices = defaultdict(list)
        for i, val in enumerate(nums):
            val_to_indices[val].append(i)

        ans = 0

        # Process each group of identical elements independently
        for indices in val_to_indices.values():
            # If there's only one index, no pairs can be formed
            if len(indices) < 2:
                continue

            # gcd_count maps gcd(i, k) -> frequency of occurrence in the current group
            gcd_count = defaultdict(int)

            for j in indices:
                gcd_j = gcd(j, k)

                # Check all previously observed gcd(i, k)
                for gcd_i, count in gcd_count.items():
                    # (i * j) % k == 0 is equivalent to (gcd(i, k) * gcd(j, k)) % k == 0
                    if (gcd_i * gcd_j) % k == 0:
                        ans += count

                gcd_count[gcd_j] += 1

        return ans
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for pairs of indices $(i, j)$ such that $0 \le i < j < n$, $nums[i] == nums[j]$, and $(i \cdot j) \equiv 0 \pmod k$.

A standard brute-force approach compares all $O(n^2)$ pairs. While $n \le 100$ makes $O(n^2)$ pass easily, an interviewer at Google or Meta will almost certainly ask: *"How does this scale if $n = 10^5$?"*

To optimize:
1. **Partition by Value:** We only care about pairs where $nums[i] == nums[j]$. Thus, we can group indices by value and solve the problem independently for each distinct value.
2. **Number-Theoretic Reduction:** For two indices $i$ and $j$, $(i \cdot j)$ is divisible by $k$ if and only if:
   $$(\gcd(i, k) \cdot \gcd(j, k)) \equiv 0 \pmod k$$
   Notice that $\gcd(i, k)$ is always a divisor of $k$. The number of divisors $d(k)$ for $k \le 100$ is at most 12 (for numbers like 60, 72, 84, 90, 96), and even for $k \le 10^5$, $d(k) \le 128$.
3. **Divisor Frequency Map:** For each group of identical values, as we iterate through its indices, we maintain the count of previously seen indices grouped by their $\gcd(i, k)$. For the current index $j$, we compute $\gcd(j, k)$ and add the counts of all previous $\gcd(i, k)$ that satisfy $(\gcd(i, k) \cdot \gcd(j, k)) \pmod k == 0$.

### Step-by-Step Approach

1. **Bucket by Values:** Create a hash map mapping each unique value in `nums` to a list of its indices.
2. **Process Each Bucket:**
   - Initialize a hash map `gcd_count` to record the frequencies of $\gcd(i, k)$ for indices processed so far within the current bucket.
   - For each index $j$:
     - Compute $g_j = \gcd(j, k)$.
     - Iterate through all distinct keys $g_i$ in `gcd_count`. If $(g_i \cdot g_j) \pmod k == 0$, add `gcd_count[g_i]` to our total count.
     - Increment `gcd_count[g_j]`.
3. Return the total count accumulated across all buckets.

### Complexity Analysis

- **Time Complexity:** 
  - Grouping indices takes $O(n)$.
  - For each index, we compute $\gcd(j, k)$ in $O(\log(\min(j, k)))$.
  - The inner loop iterates over unique $\gcd(i, k)$ values, which is bounded by the number of divisors of $k$, denoted as $d(k)$.
  - Total Time: $O(n \cdot (\log k + d(k)))$. For $k \le 100$, $d(k) \le 12$, making this effectively $O(n)$, scaling seamlessly to $n = 10^5$.
- **Space Complexity:** $O(n)$ to store indices grouped by their values. The `gcd_count` map per group uses at most $O(d(k))$ space.

### Common Pitfalls / Mistakes Candidates Make

1. **Index 0 Edge Case:** Index $0$ yields $(0 \cdot j) = 0$, and $0 \pmod k == 0$ is true for any $k \ge 1$. Candidates often trip over handling $0$ in modulo or GCD arithmetic. In Python, $\gcd(0, k) = k$, which naturally handles the condition since $(k \cdot \gcd(j, k)) \pmod k == 0$.
2. **Double Counting:** Counting both $(i, j)$ and $(j, i)$ or including $i = j$. Processing elements sequentially as $i < j$ avoids duplicate pairs.
3. **Premature Optimization Mistakes:** Overcomplicating with precomputed prime factorizations when tracking $\gcd(i, k)$ is significantly simpler, bug-free, and equally optimal.

### Real Interview Follow-Up Questions

#### 1. What if the array is streamed (infinite length) and we must output the count dynamically?
Maintain a global hash map of `value -> (gcd_count map)`. For each incoming element at index $j$ with value $v$, query its associated `gcd_count`, update the total answer, and increment the frequency of $\gcd(j, k)$ in $O(d(k))$ time per stream event.

#### 2. What if $k$ is extremely large (e.g., $k \le 10^{12}$)?
Finding divisors of $k$ dynamically is still fast ($d(10^{12}) \le 6,720$). We can pre-factorize $k$ in $O(\sqrt{k})$ time and use Dirichlet convolution or precomputed divisor relations to quickly match complementary factors.

#### 3. How would you parallelize this across multiple machines?
MapReduce/Distributed processing:
- **Map phase:** Partition the input data by value: `Emit(nums[i], i)`.
- **Shuffle & Sort:** All indices belonging to the same value are gathered on the same worker node.
- **Reduce phase:** Each worker independently computes valid pairs for its assigned values using the divisor frequency approach.
- **Aggregate:** Sum up local pair counts to obtain the global total.
