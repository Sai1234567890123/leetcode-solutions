class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        """
        Determines for each query [left, right] if nums[left...right] can be rearranged
        into an arithmetic progression.
        
        Optimized to O(k) per query without sorting, yielding O(m * n) overall time complexity.
        """
        def is_arithmetic(left: int, right: int) -> bool:
            k = right - left + 1
            if k <= 2:
                # Any sequence of length <= 2 is trivially an arithmetic progression
                return True

            min_val = float('inf')
            max_val = float('-inf')

            for i in range(left, right + 1):
                val = nums[i]
                if val < min_val:
                    min_val = val
                if val > max_val:
                    max_val = val

            # Case 1: All elements must be identical (common difference is 0)
            if min_val == max_val:
                return True

            # Case 2: The span (max - min) must be evenly divisible by (k - 1)
            total_diff = max_val - min_val
            if total_diff % (k - 1) != 0:
                return False

            diff = total_diff // (k - 1)

            # Track visited progression indices to detect duplicates or invalid steps
            seen = [False] * k
            for i in range(left, right + 1):
                val = nums[i]
                offset = val - min_val

                # Must be a multiple of the common difference
                if offset % diff != 0:
                    return False

                step_idx = offset // diff
                # Check for bounds and duplicates
                if step_idx >= k or seen[step_idx]:
                    return False

                seen[step_idx] = True

            return True

        return [is_arithmetic(left, right) for left, right in zip(l, r)]
