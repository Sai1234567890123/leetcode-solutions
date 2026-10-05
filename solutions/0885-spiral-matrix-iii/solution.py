class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        total_cells = rows * cols
        result = [[rStart, cStart]]
        
        # Directions ordered: East, South, West, North (clockwise)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0  # Start facing East
        step_length = 1  # Number of steps to take in the current direction
        
        r, c = rStart, cStart
        
        while len(result) < total_cells:
            # The spiral pattern increases step length after every two turns:
            # 1 East, 1 South, 2 West, 2 North, 3 East, 3 South, etc.
            for _ in range(2):
                dr, dc = directions[d]
                for _ in range(step_length):
                    r += dr
                    c += dc
                    # Only collect coordinates that are within the grid bounds
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                        if len(result) == total_cells:
                            return result
                
                # Turn 90 degrees clockwise
                d = (d + 1) % 4
            
            # Increase length for the next pair of directions
            step_length += 1
            
        return result
