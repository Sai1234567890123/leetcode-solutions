class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        # Precompute the maximum height in each row and each column.
        # The skyline from East/West is determined by row maximums.
        # The skyline from North/South is determined by column maximums.
        row_max = [max(row) for row in grid]
        col_max = [max(grid[r][c] for r in range(n)) for c in range(n)]
        
        total_increase = 0
        
        # For each building, the maximum allowed height without altering
        # the skyline is min(row_max[r], col_max[c]).
        for r in range(n):
            r_max = row_max[r]
            for c in range(n):
                total_increase += min(r_max, col_max[c]) - grid[r][c]
                
        return total_increase
