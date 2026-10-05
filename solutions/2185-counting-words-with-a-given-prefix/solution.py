class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        """
        Counts the number of strings in 'words' that start with the prefix 'pref'.
        
        Time Complexity: O(N * L), where N is len(words) and L is len(pref).
        Space Complexity: O(1) auxiliary space.
        """
        # Python's str.startswith() is implemented in C and stops comparing
        # as soon as a mismatch occurs or the prefix length is satisfied.
        return sum(1 for word in words if word.startswith(pref))
