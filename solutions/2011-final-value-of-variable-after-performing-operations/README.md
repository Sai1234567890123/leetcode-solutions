# 2011. Final Value of Variable After Performing Operations

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/final-value-of-variable-after-performing-operations/](https://leetcode.com/problems/final-value-of-variable-after-performing-operations/)  
**Topics:** Array, String, Simulation

---

## 📝 Problem Statement

There is a programming language with only **four** operations and **one** variable `X`:

	- `++X` and `X++` **increments** the value of the variable `X` by `1`.

	- `--X` and `X--` **decrements** the value of the variable `X` by `1`.

Initially, the value of `X` is `0`.

Given an array of strings `operations` containing a list of operations, return *the **final **value of *`X` *after performing all the operations*.

 
Example 1:

```

**Input:** operations = ["--X","X++","X++"]
**Output:** 1
**Explanation:** The operations are performed as follows:
Initially, X = 0.
--X: X is decremented by 1, X =  0 - 1 = -1.
X++: X is incremented by 1, X = -1 + 1 =  0.
X++: X is incremented by 1, X =  0 + 1 =  1.

```

Example 2:

```

**Input:** operations = ["++X","++X","X++"]
**Output:** 3
**Explanation: **The operations are performed as follows:
Initially, X = 0.
++X: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
X++: X is incremented by 1, X = 2 + 1 = 3.

```

Example 3:

```

**Input:** operations = ["X++","++X","--X","X--"]
**Output:** 0
**Explanation:** The operations are performed as follows:
Initially, X = 0.
X++: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
--X: X is decremented by 1, X = 2 - 1 = 1.
X--: X is decremented by 1, X = 1 - 1 = 0.

```

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        # Initialize the variable X to 0, as per the problem description.
        x = 0
        
        # Iterate through each operation string in the input list.
        for op in operations:
            # The problem states there are only four types of operations:
            # "++X", "X++" (increment) and "--X", "X--" (decrement).
            #
            # A key observation is that all increment operations ("++X", "X++")
            # contain a '+' character, and all decrement operations ("--X", "X--")
            # contain a '-' character.
            #
            # Therefore, we can simply check for the presence of '+' to determine
            # if the operation is an increment. If '+' is not present, it must be
            # a decrement.
            if '+' in op:
                # If the operation string contains '+', it's an increment.
                x += 1
            else:
                # Otherwise (it must contain '-'), it's a decrement.
                x -= 1
                
        # After processing all operations, return the final value of X.
        return x
```

---

## 💡 Solution, Complexity & Interview Analysis

Detailed explanation not extracted.
