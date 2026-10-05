class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        total_sum = 0
        
        for i in range(n):
            # Add element from the primary diagonal
            total_sum += mat[i][i]
            
            # Add element from the secondary diagonal only if it's not the intersection
            secondary_col = n - 1 - i
            if i != secondary_col:
                total_sum += mat[i][secondary_col]
                
        return total_sum
