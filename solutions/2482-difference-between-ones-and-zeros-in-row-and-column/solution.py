class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        m = len(grid)
        n = len(grid[0])
        
        # Precompute the count of 1s in each row and each column
        ones_row = [sum(row) for row in grid]
        ones_col = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        
        # Mathematical simplification:
        # zeros_row[i] = n - ones_row[i]
        # zeros_col[j] = m - ones_col[j]
        # diff[i][j] = ones_row[i] + ones_col[j] - zeros_row[i] - zeros_col[j]
        #            = ones_row[i] + ones_col[j] - (n - ones_row[i]) - (m - ones_col[j])
        #            = 2 * ones_row[i] + 2 * ones_col[j] - (m + n)
        total_dim = m + n
        
        diff = [[0] * n for _ in range(m)]
        for i in range(m):
            row_term = 2 * ones_row[i] - total_dim
            for j in range(n):
                diff[i][j] = row_term + 2 * ones_col[j]
                
        return diff
