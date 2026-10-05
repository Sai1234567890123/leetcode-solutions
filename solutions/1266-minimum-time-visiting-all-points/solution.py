class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        total_time = 0
        
        # Traverse through each consecutive pair of points
        for i in range(len(points) - 1):
            dx = abs(points[i + 1][0] - points[i][0])
            dy = abs(points[i + 1][1] - points[i][1])
            
            # The minimum steps between two points allowing diagonal moves is
            # max(dx, dy) (Chebyshev distance / L_infinity norm).
            # Moving diagonally covers 1 horizontal and 1 vertical unit simultaneously in 1 second.
            total_time += max(dx, dy)
            
        return total_time
