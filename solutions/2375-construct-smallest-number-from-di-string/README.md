# 2375. Construct Smallest Number From DI String

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/construct-smallest-number-from-di-string/](https://leetcode.com/problems/construct-smallest-number-from-di-string/)  
**Topics:** String, Backtracking, Stack, Greedy

---

## 📝 Problem Statement

You are given a **0-indexed** string `pattern` of length `n` consisting of the characters `'I'` meaning **increasing** and `'D'` meaning **decreasing**.

A **0-indexed** string `num` of length `n + 1` is created using the following conditions:

	- `num` consists of the digits `'1'` to `'9'`, where each digit is used **at most** once.

	- If `pattern[i] == 'I'`, then `num[i]  num[i + 1]`.

Return *the lexicographically **smallest** possible string *`num`* that meets the conditions.*

 
Example 1:

```

**Input:** pattern = "IIIDIDDD"
**Output:** "123549876"
Explanation:
At indices 0, 1, 2, and 4 we must have that num[i]  num[i+1].
Some possible values of num are "245639871", "135749862", and "123849765".
It can be proven that "123549876" is the smallest possible num that meets the conditions.
Note that "123414321" is not possible because the digit '1' is used more than once.
```

Example 2:

```

**Input:** pattern = "DDD"
**Output:** "4321"
**Explanation:**
Some possible values of num are "9876", "7321", and "8742".
It can be proven that "4321" is the smallest possible num that meets the conditions.

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        """
        Constructs the lexicographically smallest number matching the DI pattern
        using a stack-based greedy approach.
        """
        result = []
        stack = []
        n = len(pattern)

        # We need to place digits 1 through n + 1
        for i in range(n + 1):
            # Push the next smallest available digit (i + 1)
            stack.append(str(i + 1))

            # Whenever we hit an 'I' or reach the end of the pattern,
            # we reverse the accumulated decreasing sequence by popping from the stack.
            if i == n or pattern[i] == 'I':
                while stack:
                    result.append(stack.pop())

        return "".join(result)
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the lexicographically smallest number formed by digits `'1'` to `'9'` without duplicates that satisfies the `'I'` (increasing) and `'D'` (decreasing) sequence constraints. 

To achieve the lexicographically smallest permutation:
1. We should strictly use the smallest possible digits: `1` through `n + 1`.
2. Whenever we have an `'I'` (or reach the end of the string), we want the digits placed so far to be finalized.
3. Whenever we encounter a sequence of `'D'`s, the subsequent digits must be strictly decreasing. A segment of $k$ consecutive `'D'`s followed by an `'I'` (or the end) means the next $k + 1$ digits should be arranged in reverse order (e.g., if we need to use digits `4, 5, 6, 7`, a decreasing sequence requires them to appear as `7, 6, 5, 4`).

A **Stack** naturally provides Last-In-First-Out (LIFO) behavior, which effortlessly reverses any contiguous sequence of decreasing transitions.

---

### Step-by-Step Approach

1. Initialize an empty stack `stack` and an output list `result`.
2. Iterate `i` from `0` to `n` (inclusive, meaning `n + 1` iterations):
   - Push the digit `str(i + 1)` onto the stack.
   - Check if we can commit the current sequence: this happens either if `i == n` (end of pattern) or `pattern[i] == 'I'`.
   - If so, pop all elements from `stack` and append them to `result`. This flips any accumulated `'D'` segments into strictly decreasing order while keeping earlier digits as small as possible.
3. Join and return `result`.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$
  - Each digit from $1$ to $n + 1$ is pushed onto the stack exactly once and popped from the stack exactly once.
  - String joining takes $\mathcal{O}(n)$ time.
  - Overall time complexity is linear with respect to the length of `pattern`. Given $n \le 8$, this executes in $< 1$ millisecond.

- **Space Complexity:** $\mathcal{O}(n)$ auxiliary space
  - The `stack` holds at most $n + 1$ elements at any given time.
  - The `result` array stores $n + 1$ characters.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Backtracking / Brute-force Permutations:**
   - Because $n \le 8$, $O((n+1)!)$ backtracking passes the test cases, but interviewers at Meta/Google will immediately ask for an optimal $O(n)$ greedy or stack-based solution.
2. **Off-by-one with string vs. digit count:**
   - A pattern of length $n$ requires a number of length $n + 1$. Forgetting the boundary condition when `i == n` leads to an incomplete result.
3. **Improper handling of multiple consecutive `'D'`s:**
   - Attempting local swaps instead of reversing the whole block can cause digits to violate earlier inequalities.

---

### Real Interview Follow-Up Questions & Answers

#### 1. What if $n$ can be up to $10^5$ and we can use any numbers from $1$ to $n+1$ (not just digits '1'-'9')?
- **Answer:** The stack approach still runs in optimal $\mathcal{O}(n)$ time and $\mathcal{O}(n)$ space. Instead of returning a string of single digits, we would return a list/array of integers: `List[int]`.

#### 2. What if we are allowed duplicate digits (e.g., minimum sum or lexicographically smallest where $num[i] \le num[i+1]$ on 'I')?
- **Answer:** If duplicates are allowed, the problem reduces to assigning numbers such that whenever we have `'I'`, we can stay equal or increment by 1. For strictly increasing/decreasing with duplicates allowed across non-adjacent positions, we would model this as finding the longest path in a DAG or using dynamic programming / greedy bounds.

#### 3. Can we solve this in $\mathcal{O}(1)$ auxiliary space?
- **Answer:** Yes. We can pre-allocate an array with numbers `[1, 2, ..., n + 1]`. Then, we iterate through `pattern`. When we see a contiguous block of `'D'`s from index `j` to `k`, we simply reverse the subarray in-place from index `j` to `k + 1` using a two-pointer reversal. This achieves $\mathcal{O}(n)$ time and $\mathcal{O}(1)$ auxiliary space (excluding the output container).
