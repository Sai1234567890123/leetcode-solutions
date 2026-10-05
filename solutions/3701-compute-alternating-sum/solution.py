class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        """
        Computes the alternating sum: nums[0] - nums[1] + nums[2] - nums[3] + ...
        
        Runs in O(N) time and O(1) auxiliary space.
        """
        total = 0
        sign = 1
        
        for num in nums:
            total += sign * num
            # Alternate sign: positive for even index, negative for odd index
            sign = -sign
            
        return total
