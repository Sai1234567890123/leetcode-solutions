class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        """
        Calculates the maximum product difference between two pairs of elements
        in nums: (largest * second_largest) - (smallest * second_smallest).
        Achieves optimal O(n) time complexity and O(1) space complexity in a single pass.
        """
        max1 = max2 = float('-inf')
        min1 = min2 = float('inf')

        for num in nums:
            # Update the two largest values
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num

            # Update the two smallest values
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        return int((max1 * max2) - (min1 * min2))
