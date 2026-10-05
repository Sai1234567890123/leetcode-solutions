class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        """
        Finds and returns the first palindromic string in the given array.
        Returns an empty string if no palindrome is found.
        """
        def is_palindrome(s: str) -> bool:
            # Two-pointer approach to avoid allocating extra memory for reversed strings
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        for word in words:
            if is_palindrome(word):
                return word
                
        return ""
