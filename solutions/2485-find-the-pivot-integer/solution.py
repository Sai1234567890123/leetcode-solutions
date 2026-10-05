import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        # Sum of integers from 1 to n: S = n * (n + 1) / 2
        # Sum from 1 to x: x * (x + 1) / 2
        # Sum from x to n: S - (x - 1) * x / 2
        # Setting them equal:
        # x * (x + 1) / 2 = S - x * (x - 1) / 2
        # => x^2 = S = n * (n + 1) / 2
        total_sum = n * (n + 1) // 2
        
        # Calculate the integer square root
        x = math.isqrt(total_sum)
        
        # If total_sum is a perfect square, x is the pivot integer
        if x * x == total_sum:
            return x
            
        return -1
