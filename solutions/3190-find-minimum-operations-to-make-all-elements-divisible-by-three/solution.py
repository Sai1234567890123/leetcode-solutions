from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Initialize a counter for the total minimum operations required.
        total_operations = 0
        
        # Iterate through each number in the input array.
        for num in nums:
            # Calculate the remainder when the current number is divided by 3.
            # For positive integers, num % 3 will always be 0, 1, or 2.
            remainder = num % 3
            
            # If the remainder is 0, the number is already divisible by 3,
            # so no operations are needed for this specific number.
            #
            # If the remainder is 1 (e.g., num = 1, 4, 7, ...):
            #   - We can subtract 1 from 'num' to make it divisible by 3 (e.g., 1 -> 0, 4 -> 3).
            #     This takes 1 operation.
            #   - Alternatively, we could add 2 to 'num' (e.g., 1 -> 3, 4 -> 6),
            #     but this would take 2 operations, which is not the minimum.
            #
            # If the remainder is 2 (e.g., num = 2, 5, 8, ...):
            #   - We can add 1 to 'num' to make it divisible by 3 (e.g., 2 -> 3, 5 -> 6).
            #     This takes 1 operation.
            #   - Alternatively, we could subtract 2 from 'num' (e.g., 2 -> 0, 5 -> 3),
            #     but this would take 2 operations, which is not the minimum.
            #
            # In both cases where the remainder is not 0 (i.e., remainder is 1 or 2),
            # exactly 1 operation is sufficient and minimum for that number.
            if remainder != 0:
                total_operations += 1
                
        # After checking all numbers in the array, return the accumulated total operations.
        return total_operations
