class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        """
        Counts the number of strings in `patterns` that appear as substrings in `word`.
        Uses Python's highly-optimized C implementation of the in-operator (Boyer-Moore-Horspool).
        """
        # Sum the boolean results where pattern is found in word
        return sum(1 for pattern in patterns if pattern in word)
