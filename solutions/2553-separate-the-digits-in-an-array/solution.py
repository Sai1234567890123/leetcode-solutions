class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        """
        Separates the digits of each integer in nums and returns them
        in the exact order of their appearance.
        """
        # List comprehension leveraging fast C-level string iteration in Python
        return [int(char) for num in nums for char in str(num)]
