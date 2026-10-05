class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """
        Finds the maximum value of (nums[i] - 1) * (nums[j] - 1) for two distinct indices i and j.
        Since all nums[i] >= 1, maximizing this expression is equivalent to finding 
        the two largest elements in the array.
        """
        max1 = 0
        max2 = 0
        
        for num in nums:
            if num > max1:
                # num is strictly greater than the current largest.
                # The old largest is now the second largest.
                max2 = max1
                max1 = num
            elif num > max2:
                # num is between max1 and max2 (or equal to max1).
                # Update max2 accordingly.
                max2 = num
                
        return (max1 - 1) * (max2 - 1)
