class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        """
        Calculates the absolute difference between the element sum 
        and the digit sum of the array nums.
        
        Note: For any positive integer x, x >= sum_of_digits(x).
        Therefore, element_sum >= digit_sum always holds, so we can 
        compute the difference directly without needing abs().
        """
        diff = 0
        
        for num in nums:
            diff += num
            curr = num
            # Extract digits iteratively using modulo and integer division
            while curr > 0:
                diff -= curr % 10
                curr //= 10
                
        return diff
