from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        
        # 1. Process diagonals in the bottom-left triangle (including main diagonal)
        # These diagonals start at grid[r][0] for r in range(n) and satisfy row - col >= 0.
        # They must be sorted in non-increasing (descending) order.
        for r in range(n):
            diag = []
            length = n - r
            for k in range(length):
                diag.append(grid[r + k][k])
            
            # Sort non-increasing
            diag.sort(reverse=True)
            
            # Write back
            for k in range(length):
                grid[r + k][k] = diag[k]

        # 2. Process diagonals in the top-right triangle
        # These diagonals start at grid[0][c] for c in range(1, n) and satisfy row - col < 0.
        # They must be sorted in non-decreasing (ascending) order.
        for c in range(1, n):
            diag = []
            length = n - c
            for k in range(length):
                diag.append(grid[k][c + k])
            
            # Sort non-decreasing
            diag.sort()
            
            # Write back
            for k in range(length):
                grid[k][c + k] = diag[k]

        return grid
