# 2160. Minimum Sum of Four Digit Number After Splitting Digits

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/](https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/)  
**Topics:** Math, Greedy, Sorting

---

## 📝 Problem Statement

You are given a **positive** integer `num` consisting of exactly four digits. Split `num` into two new integers `new1` and `new2` by using the **digits** found in `num`. **Leading zeros** are allowed in `new1` and `new2`, and **all** the digits found in `num` must be used.

	- For example, given `num = 2932`, you have the following digits: two `2`'s, one `9` and one `3`. Some of the possible pairs `[new1, new2]` are `[22, 93]`, `[23, 92]`, `[223, 9]` and `[2, 329]`.

Return *the **minimum** possible sum of *`new1`* and *`new2`.

 
Example 1:

```

**Input:** num = 2932
**Output:** 52
**Explanation:** Some possible pairs [new1, new2] are [29, 23], [223, 9], etc.
The minimum sum can be obtained by the pair [29, 23]: 29 + 23 = 52.

```

Example 2:

```

**Input:** num = 4009
**Output:** 13
**Explanation:** Some possible pairs [new1, new2] are [0, 49], [490, 0], etc. 
The minimum sum can be obtained by the pair [4, 9]: 4 + 9 = 13.

```

 
**Constraints:**

	- `1000

---

## 💻 Implementation (python3)

```py
class Solution:
    def minimumSum(self, num: int) -> int:
        # Extract and sort the 4 digits in ascending order
        digits = sorted(int(d) for d in str(num))
        
        # To minimize the sum of two numbers formed by 4 digits:
        # We must split the digits into two 2-digit numbers.
        # Place the two smallest digits in the tens places,
        # and the remaining two digits in the ones places.
        # new1 = digits[0] * 10 + digits[2]
        # new2 = digits[1] * 10 + digits[3]
        return 10 * (digits[0] + digits[1]) + digits[2] + digits[3]
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

We are given a 4-digit number and need to partition all 4 digits into two integers, $new1$ and $new2$, such that their sum is minimized.

1. **Number of Digits per Number:**
   - A partition could be either $(1\text{ digit}, 3\text{ digits})$ or $(2\text{ digits}, 2\text{ digits})$.
   - A 3-digit number takes the form $100a + 10b + c$, multiplying one of the digits by $100$.
   - Two 2-digit numbers take the form $(10a + b) + (10c + d) = 10(a + c) + (b + d)$.
   - Because $100a \ge 10a$, assigning digits to two 2-digit numbers always yields a sum less than or equal to assigning them to a 1-digit and a 3-digit number.

2. **Greedy Assignment:**
   - To minimize $10(a + c) + (b + d)$, we should assign the smallest possible weights to the larger coefficients.
   - The coefficients are $10$ for the tens digits and $1$ for the units digits.
   - Hence, after sorting the digits $d_0 \le d_1 \le d_2 \le d_3$:
     - The two smallest digits ($d_0, d_1$) should be placed in the tens places.
     - The two largest digits ($d_2, d_3$) should be placed in the units places.
   - The resulting minimum sum is:
     $$\text{Sum} = 10 \cdot (d_0 + d_1) + (d_2 + d_3)$$

### Step-by-Step Approach

1. Extract the digits of `num` into a list and sort them in non-decreasing order: $[d_0, d_1, d_2, d_3]$.
2. Compute $10 \cdot (d_0 + d_1) + d_2 + d_3$.
3. Return the result.

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$. Extracting and sorting 4 digits takes a constant number of operations (sorting an array of fixed size 4).
- **Space Complexity:** $\mathcal{O}(1)$. An array of size 4 is used, requiring $\mathcal{O}(1)$ auxiliary space.

### Common Pitfalls / Mistakes

- **Assuming digits cannot have leading zeros:** The problem statement explicitly permits leading zeros in $new1$ and $new2$.
- **Brute force generation of all permutations:** While feasible given $4! = 24$ permutations, it is unnecessary and shows a lack of mathematical/greedy intuition.
- **Overlooking the split strategy:** Mistakenly considering 3-digit + 1-digit combinations as potentially better than 2-digit + 2-digit combinations.

### Real Interview Follow-Up Questions

1. **Generalize to $N$ digits split into $K$ numbers:**
   - *Answer:* If we have $N$ digits and want to split them into $K$ numbers to minimize the sum, the lengths of the numbers should be as balanced as possible (differing by at most 1). Sort all $N$ digits in ascending order. Distribute the digits from left to right (most significant positions first) across the $K$ numbers in round-robin fashion. This ensures the smallest digits get the largest place values (e.g., hundreds, tens).

2. **What if zero digits cannot be leading zeros (i.e., positive integers only)?**
   - *Answer:* If leading zeros are prohibited, we must ensure the leading digit of each number is non-zero. We sort digits, find the smallest non-zero digits to serve as the leading digits for the numbers, and then distribute the remaining digits (including zeros) greedily in ascending order across the remaining positions from highest weight to lowest weight.
