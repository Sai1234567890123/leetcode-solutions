# 1221. Split a String in Balanced Strings

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/split-a-string-in-balanced-strings/](https://leetcode.com/problems/split-a-string-in-balanced-strings/)  
**Topics:** String, Greedy, Counting

---

## 📝 Problem Statement

**Balanced** strings are those that have an equal quantity of `'L'` and `'R'` characters.

Given a **balanced** string `s`, split it into some number of substrings such that:

	- Each substring is balanced.

Return *the **maximum** number of balanced strings you can obtain.*

 
Example 1:

```

**Input:** s = "RLRRLLRLRL"
**Output:** 4
**Explanation:** s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

```

Example 2:

```

**Input:** s = "RLRRRLLRLL"
**Output:** 2
**Explanation:** s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.
Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2nd and 5th substrings are not balanced.
```

Example 3:

```

**Input:** s = "LLLLRRRR"
**Output:** 1
**Explanation:** s can be split into "LLLLRRRR".

```

 
**Constraints:**

	- `2

---

## 💻 Implementation (python3)

```py
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        """
        Greedily split the string at every point where the count of 'R' and 'L' becomes equal.
        """
        balance = 0
        balanced_count = 0
        
        for char in s:
            # Increment for 'R' and decrement for 'L' (or vice-versa)
            if char == 'R':
                balance += 1
            else:
                balance -= 1
            
            # Whenever balance returns to zero, we've found a minimal balanced substring
            if balance == 0:
                balanced_count += 1
                
        return balanced_count
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the **maximum** number of balanced substrings. 
A string is balanced if the number of `'R'`s equals the number of `'L'`s. 

Consider a running count/balance where `'R'` adds $+1$ and `'L'` adds $-1$. A substring is balanced if its net balance is $0$.
If we encounter a prefix whose balance is $0$, it is a valid balanced string. By peeling off this minimal balanced prefix immediately, the remaining suffix also maintains a total balance of $0$ (since Total Balance = Prefix Balance + Suffix Balance $\implies 0 = 0 + 0$).

A greedy choice works optimally here: splitting as early as possible guarantees the maximum number of splits. Any larger balanced substring containing smaller balanced components can always be partitioned into those smaller components, increasing the split count.

### Step-by-Step Approach

1. Initialize `balance = 0` to track the difference between counts of `'R'` and `'L'`.
2. Initialize `balanced_count = 0` to record the number of valid splits.
3. Iterate through each character in string `s`:
   - If the character is `'R'`, increment `balance` by 1.
   - If the character is `'L'`, decrement `balance` by 1.
   - If `balance == 0`, it signifies that from the end of the last split (or the beginning of the string) up to the current position, the count of `'R'` and `'L'` is equal. Increment `balanced_count` by 1.
4. Return `balanced_count`.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the length of string `s`. We iterate through the string exactly once.
- **Space Complexity:** $\mathcal{O}(1)$. We only use two integer variables (`balance` and `balanced_count`), requiring constant additional space.

### Common Pitfalls / Mistakes Candidates Make

1. **Overcomplicating with Dynamic Programming or Stack:**
   - Some candidates attempt to use a stack or DP because balanced parentheses problems often require stacks. Here, the characters do not need to be properly nested (e.g., `"RL"` vs `"LR"` are both valid), so an integer counter is sufficient.
2. **Missing the Greedy Choice Proof:**
   - In an interview, the interviewer may ask *why* greedily splitting whenever `balance == 0` is guaranteed to be optimal. Candidates should clearly articulate that any split partition that is composite can be decomposed into smaller independent balance points without violating balance of the remaining string.

### Real Interview Follow-Up Questions

#### 1. What if the stream of characters is infinite / too large to fit in memory?
- **Answer:** The greedy approach processes one character at a time without needing to look ahead or store previous characters. We can process the input as an iterator / generator / data stream in $\mathcal{O}(1)$ space, emitting an event or incrementing a counter whenever `balance == 0`.

#### 2. What if there are more than two characters (e.g., `'R'`, `'L'`, and `'U'`, `'D'`) requiring all to have equal counts?
- **Answer:** 
  - If we need equal counts of $k$ characters, a single scalar `balance` is insufficient.
  - Instead, we track a state representing relative differences, e.g., tuple `(count('R') - count('L'), count('R') - count('U'), ...)`. 
  - The substring is balanced when all relative differences return to zero. The greedy strategy still holds: split whenever all counts match.

#### 3. What if the input string itself is NOT guaranteed to be balanced initially?
- **Answer:** 
  - If the input string is not balanced, the final segment after the last point where `balance == 0` will have a non-zero balance and cannot form a valid balanced substring.
  - In that case, the greedy split count would still represent the maximum balanced substrings if leftover trailing unbalanced characters can be discarded. If all characters must be used, and the overall string is unbalanced, the answer would be $0$ (impossible to partition into all-balanced substrings).
