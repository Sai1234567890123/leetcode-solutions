class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        # Reverse the prefix of length k, and append the remaining suffix unchanged
        return s[:k][::-1] + s[k:]
