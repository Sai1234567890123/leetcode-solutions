class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        # Pythonic solution: concatenate the original list with its reversed version.
        # nums[::-1] creates a new list that is the reverse of nums.
        # This operation is efficient, typically O(n) time and O(n) space for the new list.
        # The '+' operator concatenates two lists, creating a third new list.
        # This operation is also efficient, typically O(n) time and O(n) space for the new list.
        return nums + nums[::-1]
