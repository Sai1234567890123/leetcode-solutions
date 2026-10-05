class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        # Phase 1: Encode both the original value and the target value into each element.
        # We use the property that all numbers are in the range [0, n-1].
        # Each nums[i] will store two pieces of information:
        # 1. The original value of nums[i] (which can be retrieved by nums[i] % n).
        # 2. The target value for ans[i], which is nums[nums[i]] (this will be stored as a multiple of n,
        #    and can be retrieved by nums[i] // n after encoding).
        # The formula used is: new_nums[i] = (original_nums[i]) + (target_value * n)
        for i in range(n):
            # original_val_at_i: This is the original value of nums[i].
            # We use nums[i] % n to get the original value, in case nums[i] was already encoded
            # in a previous iteration (though for the current index i, nums[i] is still its original value
            # before this line, but it's good practice to use % n for consistency and robustness).
            original_val_at_i = nums[i] % n 
            
            # value_to_store_at_i: This is the value that should become ans[i], i.e., nums[nums[i]].
            # We need to access nums[original_val_at_i]. Since original_val_at_i is an index,
            # nums[original_val_at_i] might have already been encoded if original_val_at_i < i.
            # So, we retrieve its original value using % n.
            value_to_store_at_i = nums[original_val_at_i] % n
            
            # Encode the target value into nums[i] by adding (value_to_store_at_i * n).
            # nums[i] now effectively holds: (original_nums[i] % n) + (value_to_store_at_i * n)
            nums[i] += value_to_store_at_i * n
        
        # Phase 2: Decode the array.
        # Now, each nums[i] contains (original_nums[i] % n) + (ans[i] * n).
        # To get ans[i], we simply perform integer division by n.
        for i in range(n):
            nums[i] //= n
            
        return nums
