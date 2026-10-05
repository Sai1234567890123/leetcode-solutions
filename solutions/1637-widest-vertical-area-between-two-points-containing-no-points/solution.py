class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        # Extract and sort only the x-coordinates, since the y-coordinates
        # have no bearing on the vertical area's width (infinite height).
        x_coords = sorted(p[0] for p in points)
        
        # Find the maximum gap between any two adjacent x-coordinates.
        max_width = 0
        for i in range(1, len(x_coords)):
            gap = x_coords[i] - x_coords[i - 1]
            if gap > max_width:
                max_width = gap
                
        return max_width
