class Solution:
    def subarraySum(self, nums: list[int]) -> int:
        n = len(nums)
        # Build prefix sum array where prefix[k] = sum(nums[0 ... k-1])
        # prefix array will have size n + 1 with prefix[0] = 0
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        total_sum = 0
        for i in range(n):
            # As specified in the problem statement
            start = max(0, i - nums[i])
            # Range sum for nums[start ... i] in O(1) time
            total_sum += prefix[i + 1] - prefix[start]
            
        return total_sum
