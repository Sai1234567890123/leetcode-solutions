# 1470. Shuffle the Array

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/shuffle-the-array/](https://leetcode.com/problems/shuffle-the-array/)  
**Topics:** Array

---

## 📝 Problem Statement

Given the array `nums` consisting of `2n` elements in the form `[x1,x2,...,xn,y1,y2,...,yn]`.

*Return the array in the form* `[x1,y1,x2,y2,...,xn,yn]`.

 
Example 1:

```

**Input:** nums = [2,5,1,3,4,7], n = 3
**Output:** [2,3,5,4,1,7] 
**Explanation:** Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

```

Example 2:

```

**Input:** nums = [1,2,3,4,4,3,2,1], n = 4
**Output:** [1,4,2,3,3,2,4,1]

```

Example 3:

```

**Input:** nums = [1,1,2,2], n = 2
**Output:** [1,2,1,2]

```

 
**Constraints:**


	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        # Preallocate the result array to avoid dynamic resizing overhead
        result = [0] * (2 * n)
        
        # Interleave elements: x_i goes to 2*i, y_i goes to 2*i + 1
        for i in range(n):
            result[2 * i] = nums[i]
            result[2 * i + 1] = nums[i + n]
            
        return result
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem provides an array of length $2n$ consisting of two halves:
- First half: $[x_1, x_2, \dots, x_n]$ located at indices $0$ through $n-1$.
- Second half: $[y_1, y_2, \dots, y_n]$ located at indices $n$ through $2n-1$.

We are tasked with interleaving these elements such that the output is $[x_1, y_1, x_2, y_2, \dots, x_n, y_n]$.

Notice the index mapping for each pair $(x_i, y_i)$ at index $i$ ($0 \le i < n$):
- $x_i = \text{nums}[i]$ is mapped to destination index $2 \cdot i$.
- $y_i = \text{nums}[i + n]$ is mapped to destination index $2 \cdot i + 1$.

By preallocating an array of length $2n$, we can populate all target positions in a single linear pass with optimal cache locality and no dynamic reallocation overhead.

---

### Step-by-Step Approach

1. **Preallocation**: Initialize a list `result` of size $2n$ with zeros.
2. **Interleaving**: Loop $i$ from $0$ to $n - 1$:
   - Place $\text{nums}[i]$ at index $2i$.
   - Place $\text{nums}[i + n]$ at index $2i + 1$.
3. **Return**: Return the populated `result` list.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$ (or $\mathcal{O}(N)$ where $N = 2n$). We iterate $n$ times, performing constant-time $\mathcal{O}(1)$ array writes per iteration.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space (excluding the output array). If the output array is counted, it takes $\mathcal{O}(n)$ total space.

---

### Common Pitfalls / Mistakes

1. **Repeated `.append()` / List Concatenation (`+`)**: Using `res.append(x); res.append(y)` incurs repeated list amortized resizes. While still $\mathcal{O}(n)$, preallocating `[0] * (2 * n)` is faster and idiomatic for known-size outputs.
2. **In-place Overwrite Bug**: Trying to modify `nums` in-place naively without an auxiliary array will overwrite elements before they are moved to their target positions (e.g., placing $y_1$ at index $1$ overwrites $x_2$).
3. **Off-by-one with Pointer Indices**: Confusing pointer offsets (e.g., using `i + n - 1` instead of `i + n`).

---

### Real Interview Follow-Up Questions

#### Follow-Up 1: Can you do this strictly in $\mathcal{O}(1)$ auxiliary space in-place?
**Answer:**
Yes, by taking advantage of the constraints or using cycle-leader permutation algorithms.
1. **Bit Manipulation (Constraint-dependent):**
   Given $1 \le \text{nums}[i] \le 10^3$, each number fits in 10 bits ($2^{10} = 1024$). Since standard integers have at least 32 bits:
   - Pack pairs into the second half of `nums`: `nums[i + n] = (nums[i] << 10) | nums[i + n]`.
   - Unpack backwards into `nums` from index $2n - 1$ down to $0$:
     - For $i$ from $0$ to $n-1$: 
       - $\text{nums}[2i] = \text{nums}[i + n] \gg 10$
       - $\text{nums}[2i + 1] = \text{nums}[i + n] \ \& \ 1023$
2. **Cycle Leader Algorithm (General / Constraint-independent):**
   Without value bounds, this is an in-place array shuffle (equivalent to matrix transpose). The mapping function is $f(i) = (2i) \bmod (2n - 1)$ for $i < 2n - 1$. We can decompose the permutation into disjoint cycles and rotate each cycle using $\mathcal{O}(1)$ extra space and $\mathcal{O}(n \log n)$ or $\mathcal{O}(n)$ time.

#### Follow-Up 2: How would you handle a streaming input where $(x_i, y_i)$ arrive asynchronously?
**Answer:**
If the stream delivers $x$'s first and then $y$'s, we need a bounded buffer or local disk spooling of size $n$ before we can emit pairs. If $x_i$ and $y_i$ arrive with sequence IDs out of order, use a hash map or priority queue/min-heap as an order-reconstruction buffer to emit pairs sequentially as soon as matching IDs arrive.

#### Follow-Up 3: How would you parallelize this for massive datasets (e.g., $N = 10^{10}$)?
**Answer:**
Because the mapping $i \to (2i, 2i+1)$ is completely embarrassingly parallel and deterministic:
- Split the input into chunks across multiple workers/threads.
- Worker $k$ processing range $[i_{\text{start}}, i_{\text{end}})$ writes directly to output offsets $[2 \cdot i_{\text{start}}, 2 \cdot i_{\text{end}})$.
- Since writes are non-overlapping, no locks or synchronization primitives are required.
