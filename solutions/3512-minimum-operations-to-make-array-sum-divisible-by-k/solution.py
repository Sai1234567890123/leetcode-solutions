class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Calculate the initial sum of all elements in the array.
        # Python's `sum()` function efficiently handles large integers,
        # so potential overflow for very large sums (up to 10^14) is not an issue.
        current_sum = sum(nums)
        
        # The goal is to perform 'X' operations such that the new sum (current_sum - X)
        # is divisible by 'k'. This can be expressed as:
        # (current_sum - X) % k == 0
        
        # Let 'remainder' be the current_sum % k.
        # We know that current_sum can be written as:
        # current_sum = q * k + remainder, where 'q' is an integer quotient.
        
        # Substituting this into our goal equation:
        # (q * k + remainder - X) % k == 0
        
        # Since (q * k) is always divisible by 'k', (q * k) % k is 0.
        # The equation simplifies to:
        # (remainder - X) % k == 0
        
        # We want the minimum non-negative value for 'X'.
        #
        # Case 1: If 'remainder' is 0 (i.e., current_sum is already divisible by k).
        # In this case, (0 - X) % k == 0 implies X must be a multiple of k.
        # The minimum non-negative X is 0.
        #
        # Case 2: If 'remainder' is not 0.
        # To make (remainder - X) % k == 0 with the minimum non-negative X,
        # we should choose X equal to 'remainder'.
        # For example, if current_sum % k = 4, we need to subtract 4 from the sum
        # to make it divisible by k. (e.g., if sum is 19 and k is 5, 19 % 5 = 4.
        # Subtracting 4 makes the sum 15, which is 15 % 5 = 0).
        
        # Calculate the remainder. This value directly represents the minimum operations needed.
        operations_needed = current_sum % k
        
        # Return the calculated minimum operations.
        return operations_needed
