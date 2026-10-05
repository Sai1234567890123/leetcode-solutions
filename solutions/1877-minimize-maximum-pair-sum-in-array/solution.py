class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        """
        Minimizes the maximum pair sum by sorting the array and pairing 
        the i-th smallest element with the i-th largest element.
        """
        nums.sort()
        
        n = len(nums)
        max_pair_sum = 0
        
        # Pair elements from the outer ends towards the center
        for i in range(n // 2):
            current_pair_sum = nums[i] + nums[n - 1 - i]
            if current_pair_sum > max_pair_sum:
                max_pair_sum = current_pair_sum
                
        return max_pair_sum
