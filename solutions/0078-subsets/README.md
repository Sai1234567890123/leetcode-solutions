# 0078. Subsets

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/subsets/](https://leetcode.com/problems/subsets/)  
**Topics:** Array, Backtracking, Bit Manipulation

---

## 📝 Problem Statement

Given an integer array `nums` of **unique** elements, return *all possible* *subsets* *(the power set)*.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

 
Example 1:

```

**Input:** nums = [1,2,3]
**Output:** [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

```

Example 2:

```

**Input:** nums = [0]
**Output:** [[],[0]]

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        current_subset: list[int] = []

        def backtrack(start_index: int) -> None:
            # Every state reached in the recursion tree represents a valid subset.
            # Append a copy of the current subset to avoid reference mutation.
            result.append(list(current_subset))

            # Explore further candidates to build subsequent subsets
            for i in range(start_index, len(nums)):
                # Decision: include nums[i]
                current_subset.append(nums[i])
                
                # Recurse to generate all subsets starting with nums[i]
                backtrack(i + 1)
                
                # Backtrack: undo the decision to explore other subsets
                current_subset.pop()

        backtrack(0)
        return result
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process
The problem asks for the power set of an array of distinct integers. For an array of length $n$, the total number of subsets is $2^n$ because every element has two independent choices: either it is included in a subset or it is excluded.

We can visualize this decision process as a recursion tree (state-space tree):
1. Start with an empty subset `[]`.
2. At each recursion level starting at `start_index`, iterate through remaining elements `nums[i]` (where $i \ge \text{start\_index}$).
3. Add `nums[i]` to our subset, recurse on index `i + 1`, and then backtrack (remove `nums[i]`) to explore choices that do not include `nums[i]`.
4. Crucially, **every intermediate state of `current_subset` is a valid subset**, so we record `current_subset` at the beginning of each recursive call.

### Step-by-Step Approach
1. **Initialize State**: Maintain a global/outer `result` list and a `current_subset` list acting as our working buffer.
2. **Recursive Function `backtrack(start_index)`**:
   - Save a snapshot (copy) of `current_subset` into `result`.
   - Loop `i` from `start_index` to `len(nums) - 1`:
     - Append `nums[i]` to `current_subset`.
     - Recursively call `backtrack(i + 1)`.
     - Pop `nums[i]` from `current_subset` (backtracking step).
3. **Execute & Return**: Call `backtrack(0)` and return `result`.

### Complexity Analysis
- **Time Complexity:** $\mathcal{O}(n \cdot 2^n)$
  - There are $2^n$ total subsets.
  - Generating and copying each subset of average length $\frac{n}{2}$ to the results list takes $\mathcal{O}(n)$ time.
  - Hence, the total time complexity is bounded by $\mathcal{O}(n \cdot 2^n)$, which is optimal since outputting the result requires at least this many operations.
- **Space Complexity:** $\mathcal{O}(n)$ auxiliary space (excluding the output list)
  - The recursion call stack reaches a maximum depth of $n$.
  - The temporary `current_subset` list consumes up to $\mathcal{O}(n)$ space.
  - The returned output list consumes $\mathcal{O}(n \cdot 2^n)$ memory.

---

### Common Pitfalls / Mistakes Candidates Make
1. **Shallow Copy Bug:**
   - Writing `result.append(current_subset)` instead of `result.append(list(current_subset))` or `result.append(current_subset[:])`. Since `current_subset` is mutated in-place, without creating a copy, all entries in `result` end up referencing the same empty list `[]` at the end.
2. **Off-by-One / Reusing Elements:**
   - Passing `i` instead of `i + 1` into the recursive call, which would generate combinations with replacement (infinite loop if unbounded).
3. **Redundant Base Cases:**
   - Adding explicit base cases like `if start_index == len(nums): return`. While not wrong, the `for` loop condition `range(start_index, len(nums))` inherently terminates the recursion when `start_index == len(nums)`.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if the input array contains duplicate elements? (LeetCode 90: Subsets II)
*Answer:* 
Sort the input array first. During the loop in `backtrack`, skip duplicate elements that appear at the same tree depth:
```python
if i > start_index and nums[i] == nums[i - 1]:
    continue
```
This ensures we only branch on the first occurrence of identical elements at any given decision level, avoiding duplicate subsets.

#### 2. Can you generate subsets iteratively without recursion?
*Answer:*
Yes, in two ways:
1. **Cascading:** Start with `result = [[]]`. For each number `x` in `nums`, duplicate all existing subsets in `result` and append `x` to them:
   ```python
   result = [[]]
   for x in nums:
       result += [curr + [x] for curr in result]
   ```
2. **Bitmasking:** Loop an integer $mask$ from $0$ to $2^n - 1$. The $j$-th bit of $mask$ determines whether `nums[j]` is included in the subset.

#### 3. What if $n$ is very large (e.g., $n = 60$) and the power set cannot fit in memory?
*Answer:*
$2^{60}$ subsets is an astronomical number (~$1.15 \times 10^{18}$) that cannot be stored in RAM or generated in practical time.
- **Generator / Stream Pattern:** Instead of collecting all subsets in a list, convert the function into a Python generator using `yield` (or an Iterator in Java/C++). This keeps memory consumption at $\mathcal{O}(n)$.
- **Distributed Generation:** Divide the bitmask space $[0, 2^n - 1]$ across a distributed computing cluster (e.g., MapReduce / Spark), where worker nodes process distinct disjoint ranges of integers and write outputs to distributed storage (S3/HDFS).
