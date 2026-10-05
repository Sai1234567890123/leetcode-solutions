# 3945. Digit Frequency Score

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/digit-frequency-score/](https://leetcode.com/problems/digit-frequency-score/)  
**Topics:** Hash Table, Math

---

## 📝 Problem Statement

You are given an integer `n`.

The **score** of `n` is defined as the **sum** of `d * freq(d)` over all **distinct** digits `d`, where `freq(d)` denotes the number of times the digit `d` appears in `n`.

Return an integer denoting the score of `n`.

 
Example 1:

**Input:** n = 122

**Output:** 5

**Explanation:**

	- The digit 1 appears 1 time, contributing `1 * 1 = 1`.

	- The digit 2 appears 2 times, contributing `2 * 2 = 4`.

	- Thus, the score of `n` is `1 + 4 = 5`.

Example 2:

**Input:** n = 101

**Output:** 2

**Explanation:**

	- The digit 0 appears 1 time, contributing `0 * 1 = 0`.

	- The digit 1 appears 2 times, contributing `1 * 2 = 2`.

	- Thus, the score of `n` is 2.

 
**Constraints:**

	- `1 9`

---

## 💻 Implementation (python3)

```py
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        # Initialize an array to store the frequency of each digit (0-9).
        # The index represents the digit, and the value represents its frequency.
        # This array has a fixed size of 10, making space complexity O(1).
        counts = [0] * 10

        # Use a temporary variable to extract digits without modifying the original 'n'.
        # The problem constraints state 1 <= n <= 10^9, so n will always be positive.
        # This loop will run at least once (e.g., for n=1, it runs once; for n=122, it runs thrice).
        temp_n = n
        while temp_n > 0:
            # Get the last digit of temp_n using the modulo operator.
            digit = temp_n % 10
            
            # Increment the frequency count for this digit.
            counts[digit] += 1
            
            # Remove the last digit from temp_n using integer division to process the next digit.
            temp_n //= 10

        # Calculate the total score based on the frequencies.
        total_score = 0
        # Iterate through all possible digits from 0 to 9.
        for d in range(10):
            # If the digit 'd' appeared in 'n' (i.e., its frequency is greater than 0),
            # add its contribution to the total score.
            if counts[d] > 0:
                # The contribution for a digit 'd' is d multiplied by its frequency (d * freq(d)).
                total_score += d * counts[d]
        
        # Return the final calculated score.
        return total_score
```

---

## 💡 Solution, Complexity & Interview Analysis

## Intuition & Thought Process

The problem asks us to calculate a "score" for a given integer `n`. The score is defined as the sum of `d * freq(d)` for all distinct digits `d` present in `n`, where `freq(d)` is the number of times digit `d` appears in `n`.

Let's break down the process with an example, `n = 122`:
1.  **Identify digits and their counts**:
    *   The digits in `122` are `1`, `2`, `2`.
    *   Digit `1` appears once (`freq(1) = 1`).
    *   Digit `2` appears twice (`freq(2) = 2`).
2.  **Calculate contribution for each distinct digit**:
    *   For digit `1`: `1 * freq(1) = 1 * 1 = 1`.
    *   For digit `2`: `2 * freq(2) = 2 * 2 = 4`.
3.  **Sum contributions**:
    *   Total score = `1 + 4 = 5`.

The core idea is to first determine the frequency of each digit (0-9) within the input number `n`. Once we have these frequencies, we can iterate through the digits 0-9 and, for each digit that appeared in `n`, calculate its contribution (`d * freq(d)`) and add it to a running total.

## Step-by-Step Approach

1.  **Initialize Frequency Counter**: Create an array (or list in Python) of size 10, say `counts`, initialized with zeros. `counts[i]` will store the frequency of digit `i`.
2.  **Extract Digits and Count Frequencies**:
    *   Use a temporary variable, `temp_n`, initialized with the input `n`.
    *   Repeatedly perform the following operations until `temp_n` becomes 0:
        *   Get the last digit of `temp_n` using the modulo operator: `digit = temp_n % 10`.
        *   Increment the count for this `digit` in our `counts` array: `counts[digit] += 1`.
        *   Remove the last digit from `temp_n` using integer division: `temp_n //= 10`.
    *   *Edge Case Consideration*: The problem constraints state `1 <= n <= 10^9`. This means `n` will always be positive, so the `while temp_n > 0` loop will always execute at least once. If `n` could be 0, an explicit check `if n == 0: counts[0] = 1` would be needed before the loop, but it's not required here.
3.  **Calculate Total Score**:
    *   Initialize a variable `total_score = 0`.
    *   Iterate through the digits `d` from 0 to 9 (inclusive).
    *   For each `d`, check if `counts[d]` is greater than 0. This indicates that digit `d` was present in the original number `n`.
    *   If `counts[d] > 0`, calculate its contribution: `d * counts[d]`, and add this to `total_score`.
4.  **Return Result**: After iterating through all digits, `total_score` will hold the final score. Return `total_score`.

## Complexity Analysis

*   **Time Complexity**:
    *   **Digit Extraction**: The `while` loop runs once for each digit in `n`. The number of digits in `n` is proportional to `log10(n)`. For `n <= 10^9`, `n` has at most 10 digits. Each operation inside the loop (`%`, `//`, array access) is O(1). Thus, this part takes O(log n) time, which is effectively O(D) where D is the number of digits.
    *   **Score Calculation**: The `for` loop iterates 10 times (for digits 0-9). Each operation inside the loop is O(1). Thus, this part takes O(10), which simplifies to O(1) time.
    *   **Total Time Complexity**: O(log n) or O(D), where D is the number of digits in `n`. Given the constraints, D is very small (at most 10), so this is extremely efficient, almost constant time.

*   **Space Complexity**:
    *   We use a `counts` array of fixed size 10 to store digit frequencies. This array's size does not depend on the magnitude of `n`.
    *   **Total Space Complexity**: O(1).

## Common Pitfalls / Mistakes

1.  **Incorrectly Handling `n=0`**: Although the problem constraints (`1 <= n <= 10^9`) prevent `n` from being 0, if it were allowed, the `while temp_n > 0` loop would not execute, leaving all counts at zero. The score for `n=0` should be `0 * 1 = 0`. A simple `if n == 0: counts[0] = 1` before the loop would fix this if `n=0` was a valid input.
2.  **Confusing Digit Value with Frequency**: A common error is to sum `d` or `freq(d)` instead of their product `d * freq(d)`. Always double-check the problem's exact scoring formula.
3.  **Using Inefficient Data Structures**: While a hash map (dictionary) for `counts` would work, an array of size 10 is more optimal for fixed, small integer keys (0-9) due to direct indexing and no hashing overhead.
4.  **String Conversion Overhead (Minor)**: Converting `n` to a string (`str(n)`) and iterating through characters is also a valid approach. For `n <= 10^9`, this is perfectly acceptable and has the same asymptotic complexity. However, integer arithmetic (`%` and `//`) can sometimes be marginally faster in performance-critical scenarios as it avoids string object creation and parsing.

## Real Interview Follow-Up Questions

1.  **What if `n` could be very large, say up to `10^1000` (a number with 1000 digits)?**
    *   **Answer**: In Python, integers handle arbitrary precision, so the current `n % 10` and `n //= 10` approach would still work directly. The time complexity would scale linearly with the number of digits, becoming O(D) where D is the number of digits (e.g., 1000). The space complexity for the `counts` array would remain O(1).
    *   In languages like C++ or Java, `n` would typically be passed as a string for such large numbers. In that case, we would iterate through the characters of the string, convert each character to an integer digit, and update the `counts` array. The complexity would still be O(D) time and O(1) space (for the `counts` array, plus O(D) for the input string itself).

2.  **What if we need to calculate scores for a stream of numbers?**
    *   **Answer**: If each number in the stream needs its individual score, we would simply call the `digitFrequencyScore(n)` function for each number. The complexity per number remains O(D) time and O(1) space.
    *   If the problem implies a *cumulative* score or an aggregate over the entire stream (e.g., total score of all numbers, or frequencies of digits across all numbers), we would adapt. For a total score, we'd sum the results of `digitFrequencyScore` for each number. For aggregate digit frequencies, we'd maintain a single `counts` array across all numbers in the stream, updating it for each number, and then calculate the final score once at the end.

3.  **What if memory is extremely constrained, and `n` is so large it cannot fit in memory (e.g., `10^1000000`)?**
    *   **Answer**: The `counts` array itself is O(1) space (10 integers), so it's very memory efficient. The primary memory concern would be storing `n` itself. If `n` is too large to fit in memory as a string or a large integer object, it would likely be provided as a file or a sequence of characters from an input stream. In this scenario, we would read `n` digit by digit (e.g., character by character from a file), update the `counts` array, and never store the full `n` in memory. This approach would still maintain O(D) time complexity (where D is the number of digits read) and O(1) space complexity (for the `counts` array).

4.  **What if the problem asked for the score of digits in a different base (e.g., base 16 for hexadecimal digits A-F)?**
    *   **Answer**: The core logic remains adaptable.
        *   If `n` is given in base 10, but we need to find digits in base `B`: We would repeatedly take `n % B` to get the digit and `n //= B` to reduce `n`. The `counts` array would need to be of size `B` (e.g., 16 for hexadecimal). The score calculation would then sum `d * counts[d]` for `d` from 0 to `B-1`.
        *   If `n` is given as a string representation in base `B`: We would iterate through the characters of the string. For each character, convert it to its integer value (e.g., 'A' -> 10, 'F' -> 15). Update the `counts` array (size `B`). Then calculate the score.
    *   The complexity would be O(log_B(n)) time and O(B) space for the counts array.

5.  **What if the problem asked for the score of *unique* digits, where `freq(d)` is always 1 for any digit present?**
    *   **Answer**: The first step of counting frequencies would remain the same. However, in the score calculation step, instead of `total_score += d * counts[d]`, we would simply add `d` if `counts[d] > 0`. For example, for `n = 122`, the original score is `1*1 + 2*2 = 5`. With unique digit scoring, it would be `1 + 2 = 3`. This is a minor modification to the final summation loop.
