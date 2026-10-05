class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        start_r, start_c = 0, 0
        # Count total non-obstacle squares that must be visited.
        # Include start (1) and empty squares (0).
        empty_count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    start_r, start_c = r, c
                    empty_count += 1
                elif grid[r][c] == 0:
                    empty_count += 1

        total_paths = 0

        def backtrack(r: int, c: int, remaining: int) -> None:
            nonlocal total_paths
            
            # Base case: Reached the ending square
            if grid[r][c] == 2:
                # Valid path only if all empty squares and start square have been visited
                if remaining == 0:
                    total_paths += 1
                return

            # Mark current square as visited by temporarily setting it to an obstacle
            temp = grid[r][c]
            grid[r][c] = -1

            # Explore all 4 orthogonal directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != -1:
                    backtrack(nr, nc, remaining - 1)

            # Backtrack / unmark the current square
            grid[r][c] = temp

        # Start backtracking from the starting cell.
        # remaining represents non-obstacle squares (excluding end cell '2') left to step off from.
        backtrack(start_r, start_c, empty_count)
        return total_paths
