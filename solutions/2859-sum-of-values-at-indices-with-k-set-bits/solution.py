class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        """
        Calculates the sum of elements at indices that have exactly k set bits.
        """
        total_sum = 0
        for i, val in enumerate(nums):
            # int.bit_count() is introduced in Python 3.10 and runs in O(1) time
            # utilizing hardware POPCNT instructions where available.
            if i.bit_count() == k:
                total_sum += val
                
        return total_sum
