class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        # Calculate the absolute distance from each person to Person 3 (at position z)
        dist1 = abs(x - z)
        dist2 = abs(y - z)
        
        # Since both move at the same speed, shorter distance means earlier arrival
        if dist1 < dist2:
            return 1
        elif dist2 < dist1:
            return 2
        else:
            return 0
