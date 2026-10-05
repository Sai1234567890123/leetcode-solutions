class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        # Result matrix dimensions are (n - 2) x (n - 2)
        max_local = [[0] * (n - 2) for _ in range(n - 2)]
        
        # Iterate over all possible top-left corners of 3x3 submatrices
        for i in range(n - 2):
            for j in range(n - 2):
                # Find maximum value in the 3x3 window:
                # rows: i to i + 2, cols: j to j + 2
                max_val = 0
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if grid[r][c] > max_val:
                            max_val = grid[r][c]
                max_local[i][j] = max_val
                
        return max_local
