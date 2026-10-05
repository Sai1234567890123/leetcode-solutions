# 3760. Maximum Substrings With Distinct Start

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/maximum-substrings-with-distinct-start/](https://leetcode.com/problems/maximum-substrings-with-distinct-start/)  
**Topics:** Hash Table, String

---

## 📝 Problem Statement

You are given a string `s` consisting of lowercase English letters.

Return an integer denoting the **maximum** number of substrings you can split `s` into such that each **substring** starts with a **distinct** character (i.e., no two substrings start with the same character).

 
Example 1:

**Input:** s = "abab"

**Output:** 2

**Explanation:**

	- Split `"abab"` into `"a"` and `"bab"`.

	- Each substring starts with a distinct character i.e `'a'` and `'b'`. Thus, the answer is 2.

Example 2:

**Input:** s = "abcd"

**Output:** 4

**Explanation:**

	- Split `"abcd"` into `"a"`, `"b"`, `"c"`, and `"d"`.

	- Each substring starts with a distinct character. Thus, the answer is 4.

Example 3:

**Input:** s = "aaaa"

**Output:** 1

**Explanation:**

	- All characters in `"aaaa"` are `'a'`.

	- Only one substring can start with `'a'`. Thus, the answer is 1.

 
**Constraints:**

	- `1 5`

	- `s` consists of lowercase English letters.

---

## 💻 Implementation (python3)

```py
class Solution:
    def maxDistinct(self, s: str) -> int:
        # The problem asks for the maximum number of substrings we can split 's' into
        # such that each substring starts with a distinct character.
        #
        # Let's denote the split as s = s_1 + s_2 + ... + s_k.
        # The starting characters are s_1[0], s_2[0], ..., s_k[0].
        # These k characters must all be distinct. We want to maximize k.
        #
        # Consider the set of all unique characters present in the string 's'.
        # Let this set be U. The maximum possible value for k is |U|,
        # because we cannot have more distinct starting characters than there are
        # unique characters available in the string itself.
        #
        # We need to show that we can always achieve |U| distinct starting characters.
        # Let the unique characters in 's' be c_1, c_2, ..., c_m, where m = |U|.
        # We can construct a valid split using a greedy approach:
        #
        # 1. Initialize an empty set `seen_chars` to store characters that have already
        #    been used as a starting character for a substring.
        # 2. Initialize a counter `num_distinct_starts` to 0.
        #
        # 3. Iterate through each character `char` in the input string `s`:
        #    a. If `char` is not in `seen_chars`:
        #       This means `char` has not been used as a starting character yet.
        #       We greedily choose to start a new substring with `char` at this position.
        #       Add `char` to `seen_chars`.
        #       Increment `num_distinct_starts`.
        #    b. Else (`char` is already in `seen_chars`):
        #       This means `char` has already been used as a starting character for an
        #       earlier substring. We cannot use it again for a new substring.
        #       Therefore, this `char` must be part of the current (last-started) substring.
        #       Do nothing.
        #
        # After iterating through the entire string, `num_distinct_starts` will hold
        # the maximum number of distinct starting characters.
        #
        # Why is this greedy approach optimal and equivalent to `len(set(s))`?
        # Let `U_s` be the set of all unique characters in the string `s`.
        # Let `G_set` be the `seen_chars` set at the end of the greedy algorithm.
        #
        # 1. `G_set` is a subset of `U_s`: Any character added to `G_set` must be
        #    present in `s`. So, `G_set \subseteq U_s`.
        # 2. `U_s` is a subset of `G_set`: Consider any character `c` in `U_s`.
        #    Let `j` be the *first index* in `s` where `s[j] = c`.
        #    When the greedy algorithm processes `s[j]`, `c` cannot possibly be
        #    in `seen_chars` yet, because `j` is its first occurrence in `s`.
        #    Thus, `c` will be added to `seen_chars` and `num_distinct_starts` will be incremented.
        #    This applies to every unique character in `s`. So, `U_s \subseteq G_set`.
        #
        # From (1) and (2), it follows that `G_set = U_s`.
        # Therefore, `num_distinct_starts` (which is `len(G_set)`) is equal to `len(U_s)`.
        #
        # The problem effectively asks for the number of unique characters in the string.

        # Python's `set` constructor can directly take an iterable (like a string)
        # and will automatically populate the set with unique elements from it.
        # The `len()` function then returns the number of elements in the set.
        return len(set(s))
```

---

## 💡 Solution, Complexity & Interview Analysis

## Intuition & Thought Process

The problem asks us to find the maximum number of substrings we can split a given string `s` into, such that each substring starts with a distinct character.

Let's break down the requirements:
1.  We need to split `s` into `k` substrings: `s = s_1 + s_2 + ... + s_k`. This means `s_1` starts at index 0, `s_2` starts at some index `j_1 > 0`, `s_3` starts at `j_2 > j_1`, and so on.
2.  The starting characters `s_1[0], s_2[0], ..., s_k[0]` must all be distinct.
3.  We want to maximize `k`.

Let's consider the set of all unique characters present in the string `s`. Let this set be `U_s`.
The maximum possible number of distinct starting characters we can have is `|U_s|`, because we cannot use a character as a starting character if it doesn't exist in `s`, and we cannot use more distinct characters than there are unique characters available in `s`.

The crucial insight is to determine if we can *always* achieve `|U_s|` distinct starting characters.
Consider a greedy strategy:
1.  Initialize an empty set `seen_chars` to keep track of characters already used as starting points.
2.  Initialize a counter `num_distinct_starts = 0`.
3.  Iterate through the input string `s` character by character from left to right.
    *   If the current character `char` is *not* in `seen_chars`: This means we haven't used this character as a starting point yet. To maximize `num_distinct_starts`, we should greedily use it now. We add `char` to `seen_chars` and increment `num_distinct_starts`. This implicitly marks the current position as the start of a new substring.
    *   If the current character `char` *is* already in `seen_chars`: This means we have already used `char` as a starting point for an earlier substring. We cannot use it again for a *new* substring because the starting characters must be distinct. Therefore, this `char` must simply be part of the current (last-started) substring. We do nothing.

Let's trace this with an example: `s = "abacaba"`
- `seen_chars = {}`, `num_distinct_starts = 0`
- `i = 0, s[0] = 'a'`: 'a' not in `seen_chars`. Add 'a'. `seen_chars = {'a'}`, `num_distinct_starts = 1`. (Substring 1 starts with 'a')
- `i = 1, s[1] = 'b'`: 'b' not in `seen_chars`. Add 'b'. `seen_chars = {'a', 'b'}`, `num_distinct_starts = 2`. (Substring 2 starts with 'b'. Substring 1 is `s[0...0] = "a"`)
- `i = 2, s[2] = 'a'`: 'a' *is* in `seen_chars`. Do nothing. ('a' is part of Substring 2)
- `i = 3, s[3] = 'c'`: 'c' not in `seen_chars`. Add 'c'. `seen_chars = {'a', 'b', 'c'}`, `num_distinct_starts = 3`. (Substring 3 starts with 'c'. Substring 2 is `s[1...2] = "ba"`)
- `i = 4, s[4] = 'a'`: 'a' *is* in `seen_chars`. Do nothing. ('a' is part of Substring 3)
- `i = 5, s[5] = 'b'`: 'b' *is* in `seen_chars`. Do nothing. ('b' is part of Substring 3)
- `i = 6, s[6] = 'a'`: 'a' *is* in `seen_chars`. Do nothing. ('a' is part of Substring 3)
End of string. `num_distinct_starts = 3`.
The actual split would be: `"a"`, `"ba"`, `"caba"`. The starting characters are 'a', 'b', 'c', which are distinct.

This greedy strategy works because for any unique character `c` present in `s`, let `j` be its *first occurrence* in `s`. When the algorithm reaches `s[j]`, `c` cannot possibly be in `seen_chars` yet (because `j` is its first appearance). Thus, `c` will be added to `seen_chars` and `num_distinct_starts` will be incremented. This guarantees that every unique character in `s` will eventually be counted exactly once as a distinct starting character.

Therefore, the maximum number of substrings with distinct starting characters is simply the total number of unique characters in the string `s`. In Python, this can be efficiently found using `len(set(s))`.

## Step-by-Step Approach

1.  The problem asks for the count of distinct starting characters.
2.  Any character that appears in the string `s` can potentially be a starting character.
3.  To maximize the count of distinct starting characters, we should try to use every unique character in `s` as a starting character.
4.  We can always achieve this:
    *   Let `U_s` be the set of unique characters in `s`.
    *   For each character `c` in `U_s`, find its first occurrence in `s`. Let these indices be `idx_1 < idx_2 < ... < idx_m`, where `m = |U_s|`.
    *   The characters `s[idx_1], s[idx_2], ..., s[idx_m]` are precisely all the unique characters in `s`.
    *   We can form a valid partition of `s` into `m` substrings:
        `s_1 = s[idx_1 : idx_2]`
        `s_2 = s[idx_2 : idx_3]`
        ...
        `s_{m-1} = s[idx_{m-1} : idx_m]`
        `s_m = s[idx_m : N]` (where `N` is the length of `s`)
    *   The starting characters of these `m` substrings are `s[idx_1], s[idx_2], ..., s[idx_m]`, which are all distinct.
5.  Thus, the maximum number of such substrings is simply the number of unique characters in `s`.
6.  In Python, this is directly computed by `len(set(s))`.

## Complexity Analysis

*   **Time Complexity**: O(N), where N is the length of the string `s`.
    *   Creating a `set` from a string involves iterating through each character of the string once.
    *   For each character, adding it to a hash set takes O(1) on average. Since the alphabet size is constant (26 lowercase English letters), the worst-case for set operations (e.g., hash collisions) is bounded by the alphabet size, making it effectively O(1).
    *   Therefore, the total time complexity is O(N).

*   **Space Complexity**: O(1)
    *   The `set` data structure will store at most 26 unique lowercase English letters.
    *   This maximum size is constant, regardless of the input string length N.
    *   Thus, the space complexity is O(1).

## Common Pitfalls / Mistakes

1.  **Overthinking the "split" aspect**: The problem's phrasing can lead candidates to believe they need to implement a complex dynamic programming solution or a more intricate greedy algorithm to determine the actual split points of the substrings. However, the problem only asks for the *maximum count* of distinct starting characters, not the substrings themselves. The key is realizing that any unique character in the string can be a distinct starting character in an optimal partition.
2.  **Incorrect greedy strategy**: Some might try to make substrings as short or as long as possible based on other criteria, which might not lead to the optimal count of distinct starting characters. The simple greedy approach of "count every unique character as it appears for the first time" is sufficient and correct.
3.  **Assuming a large alphabet**: While for lowercase English letters, the space complexity is O(1), if the problem allowed for a very large character set (e.g., full Unicode), the space complexity for storing unique characters would be O(K) where K is the number of unique characters, which could be up to O(N) in the worst case (all characters distinct). For the given constraints, O(1) is correct.

## Real Interview Follow-Up Questions

1.  **What if the string `s` contains characters beyond lowercase English letters (e.g., uppercase, numbers, symbols, Unicode)?**
    *   **Answer**: The core logic remains the same. Python's `set` data structure handles arbitrary hashable types, including all Unicode characters. The time complexity would still be O(N) because we iterate through the string once. The space complexity would become O(K) where K is the number of unique characters in the string. In the worst case (all characters distinct), K could be up to N, making the space complexity O(N). For a fixed, small alphabet (like ASCII or specific character sets), it remains O(1).

2.  **What if `s` is a very long string, potentially too large to fit into memory entirely (streaming data)?**
    *   **Answer**: If `s` is a stream, we cannot use `set(s)` directly as it would require loading the entire string into memory. Instead, we would process the stream character by character. We'd maintain a `set` of `seen_chars` (or a boolean array of size 256 for ASCII, or 26 for lowercase English letters) to track distinct characters encountered so far. For each character read from the stream, if it's not in `seen_chars`, we add it and increment a counter. This approach has O(1) space complexity (for a fixed alphabet size) and O(N) time complexity (where N is the total number of characters in the stream). This is precisely the greedy algorithm described in the thought process.

3.  **What if we also need to return the actual substrings, not just the count?**
    *   **Answer**: We would modify the greedy algorithm to explicitly track split points. We'd iterate through the string, maintaining `last_split_index = 0`. When we encounter a character `s[i]` that is *not* in `seen_chars`, it signifies the start of a new substring. The substring ending just before `s[i]` (i.e., `s[last_split_index : i]`) would be added to our list of results, and `last_split_index` would be updated to `i`. After the loop finishes, the final substring `s[last_split_index : N]` (from the last split point to the end of the string) would be added. This would take O(N) time and O(N) space to store the substrings.

    *   Example for `s = "abacaba"`:
        `seen_chars = set()`, `result_substrings = []`, `last_split_idx = 0`
        - `i=0, s[0]='a'`: 'a' not in `seen_chars`. Add 'a'. `seen_chars={'a'}`.
        - `i=1, s[1]='b'`: 'b' not in `seen_chars`. Add 'b'. `seen_chars={'a','b'}`.
            `result_substrings.append(s[last_split_idx : 1])` -> `result_substrings=["a"]`. `last_split_idx = 1`.
        - `i=2, s[2]='a'`: 'a' in `seen_chars`.
        - `i=3, s[3]='c'`: 'c' not in `seen_chars`. Add 'c'. `seen_chars={'a','b','c'}`.
            `result_substrings.append(s[last_split_idx : 3])` -> `result_substrings=["a", "ba"]`. `last_split_idx = 3`.
        - `i=4, s[4]='a'`: 'a' in `seen_chars`.
        - `i=5, s[5]='b'`: 'b' in `seen_chars`.
        - `i=6, s[6]='a'`: 'a' in `seen_chars`.
        - End loop.
        - `result_substrings.append(s[last_split_idx : N])` -> `result_substrings=["a", "ba", "caba"]`.
        Return `result_substrings`.

4.  **Could there be a scenario where using a character `c` later (even if it's its first occurrence) allows for a better overall count?**
    *   **Answer**: No. The goal is to maximize the *number* of distinct starting characters. If a character `c` appears for the first time at index `j`, and we *don't* use it as a starting character at `j` (meaning it becomes part of a substring that started *before* `j`), then we permanently lose the opportunity to use `c` as a distinct starting character. Since we want to maximize the count, we should always seize the opportunity to add a new distinct starting character as soon as its first occurrence is encountered. This confirms the greedy choice is optimal.
