class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        current_subset: list[int] = []

        def backtrack(start_index: int) -> None:
            # Every state reached in the recursion tree represents a valid subset.
            # Append a copy of the current subset to avoid reference mutation.
            result.append(list(current_subset))

            # Explore further candidates to build subsequent subsets
            for i in range(start_index, len(nums)):
                # Decision: include nums[i]
                current_subset.append(nums[i])
                
                # Recurse to generate all subsets starting with nums[i]
                backtrack(i + 1)
                
                # Backtrack: undo the decision to explore other subsets
                current_subset.pop()

        backtrack(0)
        return result
