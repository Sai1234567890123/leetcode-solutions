class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        """
        Returns the smallest positive integer that is a multiple of both 2 and n (i.e., lcm(2, n)).
        If n is already even, the answer is n.
        If n is odd, the answer is 2 * n.
        """
        # If n is odd (n & 1 == 1), shift left by 1 (multiply by 2).
        # If n is even (n & 1 == 0), shift left by 0 (keep n as is).
        return n << (n & 1)
