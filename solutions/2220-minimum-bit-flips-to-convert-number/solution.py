class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        """
        Calculates the minimum number of bit flips to convert start to goal.
        This is equivalent to finding the Hamming distance between the two numbers.
        """
        # XOR produces a 1 at each bit position where start and goal differ.
        diff = start ^ goal
        
        # Brian Kernighan's Algorithm to count set bits:
        # diff & (diff - 1) clears the lowest set bit.
        flips = 0
        while diff > 0:
            diff &= diff - 1
            flips += 1
            
        return flips
        
        # Note: In Python 3.10+, this can also be directly written as:
        # return (start ^ goal).bit_count()
