class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        """
        Calculates the absolute difference between the sum of elements to the left
        and the sum of elements to the right of each index.
        
        Time Complexity: O(n)
        Auxiliary Space Complexity: O(1) (excluding the output array)
        """
        left_sum = 0
        right_sum = sum(nums)
        answer = []
        
        for num in nums:
            # Exclude current element from right_sum to represent the sum of elements to its right
            right_sum -= num
            
            # Compute the absolute difference between left and right prefix sums
            answer.append(abs(left_sum - right_sum))
            
            # Include current element in left_sum for subsequent elements
            left_sum += num
            
        return answer
