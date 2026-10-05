from bisect import bisect_left, bisect_right

class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        # Sort points by their x-coordinates to allow pruning queries via binary search
        points.sort(key=lambda p: p[0])
        x_coords = [p[0] for p in points]
        
        ans = []
        for cx, cy, r in queries:
            r_squared = r * r
            
            # Points inside the circle must satisfy: cx - r <= px <= cx + r
            left_idx = bisect_left(x_coords, cx - r)
            right_idx = bisect_right(x_coords, cx + r)
            
            count = 0
            for i in range(left_idx, right_idx):
                px, py = points[i]
                dx = px - cx
                dy = py - cy
                # Euclidean distance squared comparison to avoid floating-point errors
                if dx * dx + dy * dy <= r_squared:
                    count += 1
            
            ans.append(count)
            
        return ans
