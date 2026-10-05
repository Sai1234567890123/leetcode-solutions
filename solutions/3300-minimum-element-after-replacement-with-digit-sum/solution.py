class Solution:
    def minElement(self, nums: list[int]) -> int:
        """
        Calculates the minimum element after replacing each number with its digit sum.
        Time Complexity: O(N * D) where N is the length of nums and D is the max digits (~5).
        Space Complexity: O(1) auxiliary space.
        """
        min_sum = float('inf')
        
        for num in nums:
            digit_sum = 0
            curr = num
            # Extract digits arithmetically to avoid string conversion overhead
            while curr > 0:
                digit_sum += curr % 10
                curr //= 10
            
            if digit_sum < min_sum:
                min_sum = digit_sum
                # Optimization: 1 is the theoretical minimum digit sum for any positive integer
                if min_sum == 1:
                    return 1
                    
        return min_sum
