import math

class Solution:
    def findGCD(self, nums: list[int]) -> int:
        """
        Finds the GCD of the smallest and largest number in the array.
        Time Complexity: O(N + log(min_val))
        Space Complexity: O(1)
        """
        # Single pass to find the minimum and maximum values
        min_val = float('inf')
        max_val = float('-inf')
        
        for num in nums:
            if num < min_val:
                min_val = num
            if num > max_val:
                max_val = num
                
        # Euclidean algorithm to compute gcd(min_val, max_val)
        # We can implement it iteratively to ensure O(1) auxiliary space
        a, b = min_val, max_val
        while b:
            a, b = b, a % b
            
        return a
