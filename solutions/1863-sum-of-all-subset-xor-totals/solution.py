class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        # Initialize 'or_all_nums' to 0. This variable will store the bitwise OR
        # of all elements in the 'nums' array.
        # A bit at position 'k' in 'or_all_nums' will be 1 if and only if
        # at least one number in 'nums' has its k-th bit set.
        or_all_nums = 0
        
        # Iterate through each number in the input array.
        for num in nums:
            # Perform a bitwise OR operation with the current number.
            # This accumulates all set bits from all numbers into 'or_all_nums'.
            or_all_nums |= num
        
        # Get the number of elements in the input array.
        # According to the problem constraints (1 <= nums.length <= 12),
        # 'n' will always be at least 1.
        n = len(nums)
        
        # The core mathematical property:
        # The sum of all subset XOR totals for an array 'nums' is equal to
        # (bitwise OR of all elements in 'nums') * (2^(n-1)).
        #
        # Intuition for this property:
        # Consider any specific bit position 'k'.
        # 1. If the k-th bit is 0 in ALL numbers in 'nums':
        #    Then, for any subset, its XOR total will also have its k-th bit as 0.
        #    So, this bit position contributes 0 to the total sum.
        #    This corresponds to the k-th bit of 'or_all_nums' being 0.
        #
        # 2. If the k-th bit is 1 in AT LEAST ONE number in 'nums':
        #    Let 'x' be an element in 'nums' that has its k-th bit set.
        #    We can pair up all 2^n subsets: for every subset 'A' that does NOT
        #    contain 'x', there's a corresponding subset 'A U {x}' that DOES
        #    contain 'x'.
        #    If the XOR total of 'A' has its k-th bit as 'b', then the XOR total
        #    of 'A U {x}' (which is XOR_total(A) ^ x) will have its k-th bit as 'b ^ 1'.
        #    This means that exactly half of the 2^n subsets will have their
        #    XOR total with the k-th bit set to 1, and the other half will have it as 0.
        #    So, 2^(n-1) subsets will contribute 2^k to the total sum for this bit position.
        #    This corresponds to the k-th bit of 'or_all_nums' being 1.
        #
        # Therefore, the total sum is equivalent to summing (2^(n-1) * 2^k) for
        # every bit position 'k' where the k-th bit of 'or_all_nums' is 1.
        # This simplifies to 'or_all_nums * 2^(n-1)'.
        
        # Calculate 2^(n-1) using a left bit shift for efficiency.
        # (1 << (n - 1)) is equivalent to 2 raised to the power of (n - 1).
        power_of_two_n_minus_1 = 1 << (n - 1)
        
        # Return the product as the final sum.
        return or_all_nums * power_of_two_n_minus_1
