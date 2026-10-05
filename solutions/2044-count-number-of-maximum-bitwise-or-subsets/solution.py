class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        # The bitwise OR operation is monotonically non-decreasing.
        # Therefore, the maximum possible OR value is the OR of all elements.
        max_or = 0
        for num in nums:
            max_or |= num

        n = len(nums)

        def dfs(index: int, current_or: int) -> int:
            # Pruning optimization:
            # If the current OR has already reached max_or, adding any combination
            # of the remaining elements will still result in max_or.
            # There are (n - index) remaining elements, so there are 2^(n - index) such subsets.
            if current_or == max_or:
                return 1 << (n - index)

            # Base case: reached the end without achieving max_or
            if index == n:
                return 0

            # Branch 1: Include nums[index]
            include = dfs(index + 1, current_or | nums[index])
            # Branch 2: Exclude nums[index]
            exclude = dfs(index + 1, current_or)

            return include + exclude

        return dfs(0, 0)
