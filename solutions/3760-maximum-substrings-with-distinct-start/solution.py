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
