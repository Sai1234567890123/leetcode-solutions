from typing import List

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        # Sort the array to efficiently pair the i-th smallest
        # and i-th largest elements together.
        nums.sort()
        
        n = len(nums)
        # Minimize the sum directly to avoid redundant floating-point divisions,
        # then divide the minimum sum by 2 at the end.
        min_sum = min(nums[i] + nums[n - 1 - i] for i in range(n // 2))
        
        return min_sum / 2.0
