from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        """
        Finds the two duplicate numbers in nums in O(n) time and O(1) auxiliary space
        using bit manipulation (XOR partitioning).
        """
        n = len(nums) - 2
        
        # Step 1: XOR all elements in nums with all numbers from 0 to n - 1.
        # Elements appearing once in the ideal array and once in nums will cancel out (x ^ x = 0).
        # The two sneaky numbers appear twice in nums and once in the ideal sequence (total 3 times).
        # Thus, xor_all will equal x ^ y, where x and y are the two sneaky numbers.
        xor_all = 0
        for num in nums:
            xor_all ^= num
        for i in range(n):
            xor_all ^= i
            
        # Step 2: Find the lowest set bit (rightmost bit where x and y differ).
        diff_bit = xor_all & (-xor_all)
        
        # Step 3: Partition all numbers into two buckets based on diff_bit.
        # One bucket will isolate x, and the other will isolate y.
        x = 0
        y = 0
        
        for num in nums:
            if num & diff_bit:
                x ^= num
            else:
                y ^= num
                
        for i in range(n):
            if i & diff_bit:
                x ^= i
            else:
                y ^= i
                
        return [x, y]
