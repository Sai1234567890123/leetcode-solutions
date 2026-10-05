class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        """
        Finds the repeating number 'a' and missing number 'b' from an n x n grid.
        Uses the mathematical sum and sum of squares approach to achieve O(1) auxiliary space.
        """
        n = len(grid)
        total_elements = n * n

        # Expected sum and sum of squares for 1 to total_elements (N)
        expected_sum = total_elements * (total_elements + 1) // 2
        expected_sum_sq = total_elements * (total_elements + 1) * (2 * total_elements + 1) // 6

        actual_sum = 0
        actual_sum_sq = 0

        for row in grid:
            for val in row:
                actual_sum += val
                actual_sum_sq += val * val

        # diff1 = a - b
        diff1 = actual_sum - expected_sum
        # diff2 = a^2 - b^2 = (a - b) * (a + b)
        diff2 = actual_sum_sq - expected_sum_sq

        # sum_ab = a + b = diff2 / diff1
        sum_ab = diff2 // diff1

        # Solving the linear system:
        # a = ((a - b) + (a + b)) / 2
        # b = ((a + b) - (a - b)) / 2
        repeated = (diff1 + sum_ab) // 2
        missing = (sum_ab - diff1) // 2

        return [repeated, missing]
