# 1720. Decode XORed Array

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/decode-xored-array/](https://leetcode.com/problems/decode-xored-array/)  
**Topics:** Array, Bit Manipulation

---

## 📝 Problem Statement

There is a **hidden** integer array `arr` that consists of `n` non-negative integers.

It was encoded into another integer array `encoded` of length `n - 1`, such that `encoded[i] = arr[i] XOR arr[i + 1]`. For example, if `arr = [1,0,2,1]`, then `encoded = [1,2,3]`.

You are given the `encoded` array. You are also given an integer `first`, that is the first element of `arr`, i.e. `arr[0]`.

Return *the original array* `arr`. It can be proved that the answer exists and is unique.

 
Example 1:

```

**Input:** encoded = [1,2,3], first = 1
**Output:** [1,0,2,1]
**Explanation:** If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]

```

Example 2:

```

**Input:** encoded = [6,2,7,3], first = 4
**Output:** [4,2,0,7,4]

```

 
**Constraints:**

	- `2 4`

	- `encoded.length == n - 1`

	- `0 5`

	- `0 5`

---

## 💻 Implementation (python3)

```py
class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        """
        Decodes the XOR-encoded array using the property:
        If a ^ b = c, then b = a ^ c.
        Given arr[i] and encoded[i] = arr[i] ^ arr[i + 1],
        we have arr[i + 1] = arr[i] ^ encoded[i].
        """
        n = len(encoded) + 1
        arr = [0] * n
        arr[0] = first
        
        # Sequentially derive each next element from the current element and encoded value
        for i in range(len(encoded)):
            arr[i + 1] = arr[i] ^ encoded[i]
            
        return arr
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem gives an array `encoded` where each element satisfies:
$$\text{encoded}[i] = \text{arr}[i] \oplus \text{arr}[i + 1]$$

A fundamental property of the bitwise XOR ($\oplus$) operation is that it is its own inverse:
1. $A \oplus A = 0$
2. $A \oplus 0 = A$
3. If $A \oplus B = C$, then:
   $$A \oplus B \oplus A = C \oplus A \implies B = A \oplus C$$

Applying this to our recurrence:
$$\text{arr}[i + 1] = \text{arr}[i] \oplus \text{encoded}[i]$$

Since we are given the initial value $\text{arr}[0] = \text{first}$, we can iteratively compute each subsequent element $\text{arr}[i + 1]$ by XORing the preceding element $\text{arr}[i]$ with $\text{encoded}[i]$.

---

### Step-by-Step Approach

1. **Allocate Memory**: Create an array `arr` of size $n = \text{len}(\text{encoded}) + 1$.
2. **Initialize Base Case**: Set `arr[0] = first`.
3. **Iterative Decoding**:
   - Loop index $i$ from $0$ up to $\text{len}(\text{encoded}) - 1$.
   - Set $\text{arr}[i + 1] = \text{arr}[i] \oplus \text{encoded}[i]$.
4. **Return**: Return the reconstructed `arr`.

---

### Complexity Analysis

- **Time Complexity**: $\mathcal{O}(n)$, where $n$ is the length of the resulting array `arr`. We perform a single loop running $n - 1$ iterations with $\mathcal{O}(1)$ bitwise XOR operations per step.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space (excluding the output array $\mathcal{O}(n)$ required by the problem specification). Pre-allocating the list avoids dynamic resizing overhead.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Attempting to solve via arithmetic inverse**: Trying to use subtraction or division instead of XOR. XOR is non-linear in standard arithmetic.
2. **Dynamic resizing overhead**: Using `arr.append(...)` repeatedly inside a large loop in languages where resizing incurs reallocations (though amortized $\mathcal{O}(1)$, pre-allocating the exact size `[0] * (len(encoded) + 1)` is faster and idiomatic for production).
3. **Off-by-one errors**: Mixing up indices between `encoded` and `arr`, causing out-of-bounds index errors.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if the input stream is continuous (infinite stream of XOR values)?
- **Answer**: We can implement a generator or an iterator. We keep track of only a single integer `curr = first`. Each time a new `encoded_val` arrives from the stream:
  ```python
  curr ^= encoded_val
  yield curr
  ```
  This operates in $\mathcal{O}(1)$ memory without needing to store the history.

#### 2. What if we are given random access queries: "What is `arr[k]`?" without constructing the entire array?
- **Answer**: 
  $$\text{arr}[k] = \text{first} \oplus \left(\bigoplus_{j=0}^{k-1} \text{encoded}[j]\right)$$
  - If queries are frequent on a static `encoded` array, we can build a prefix XOR array in $\mathcal{O}(n)$ time, allowing each query to be answered in $\mathcal{O}(1)$ time.
  - If `encoded` undergoes point updates, we can store prefix XORs in a **Fenwick Tree (Binary Indexed Tree)** or **Segment Tree** using XOR as the associative combining operator to support both updates and range XOR queries in $\mathcal{O}(\log n)$ time.

#### 3. Can we parallelize this decoding process for massive datasets (e.g., across multiple GPU threads or distributed workers)?
- **Answer**: Yes. This is a classic **prefix sum / parallel scan** problem under the XOR monoid $(\mathbb{Z}, \oplus, 0)$. 
  Using Blelloch's algorithm or Kogge-Stone parallel prefix algorithm, we can compute all prefix XORs in $\mathcal{O}(\log n)$ depth/span across $\mathcal{O}(n)$ parallel processors.
