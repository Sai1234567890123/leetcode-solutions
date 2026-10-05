class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        """
        Finds the smallest index i such that the sum of the digits of nums[i] is equal to i.
        """
        for i, val in enumerate(nums):
            # Compute sum of digits mathematically to avoid string conversion overhead
            digit_sum = 0
            temp = val
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10
            
            # Since we iterate from 0 upwards, the first match is guaranteed to be the smallest
            if digit_sum == i:
                return i
                
        return -1
