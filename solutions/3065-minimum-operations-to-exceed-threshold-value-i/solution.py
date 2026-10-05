class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum number of operations to ensure all elements are >= k.
        Each operation removes the smallest element, so every element strictly less
        than k must be removed.
        """
        # Count elements strictly less than k
        return sum(1 for x in nums if x < k)
