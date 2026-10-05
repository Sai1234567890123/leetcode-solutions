class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])

        def sort_diagonal(start_r: int, start_c: int) -> None:
            """Collects, sorts, and writes back values along a diagonal."""
            # Collect elements along the diagonal
            vals = []
            r, c = start_r, start_c
            while r < m and c < n:
                vals.append(mat[r][c])
                r += 1
                c += 1

            # Sort the collected values
            vals.sort()

            # Write sorted elements back along the diagonal
            r, c = start_r, start_c
            for val in vals:
                mat[r][c] = val
                r += 1
                c += 1

        # Process diagonals starting along the first column (r, 0)
        for r in range(m):
            sort_diagonal(r, 0)

        # Process diagonals starting along the first row (0, c), skipping (0, 0) as it was covered
        for c in range(1, n):
            sort_diagonal(0, c)

        return mat
