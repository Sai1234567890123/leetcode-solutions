from typing import List
from functools import reduce
from operator import xor

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        Calculates the minimum number of bit flips required across the array
        to make the bitwise XOR of all elements equal to k.
        """
        # Compute the XOR sum of all elements in the array
        total_xor = 0
        for num in nums:
            total_xor ^= num
        
        # The differing bits between total_xor and k indicate the minimum flips needed.
        # Flipping a bit in any number flips that bit in the total XOR.
        # Thus, each differing bit requires exactly one flip.
        diff = total_xor ^ k
        
        # Return the number of set bits (popcount / Hamming weight)
        return diff.bit_count()
