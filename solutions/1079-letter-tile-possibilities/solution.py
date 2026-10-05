from collections import Counter
import math

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        Calculates the number of possible non-empty sequences of letters using
        Dynamic Programming with Exponential Generating Functions (combinatorics).
        
        dp[len] represents the number of valid sequences of length 'len' formed
        so far. When incorporating a new character with frequency 'count', we can
        choose to use 'j' instances of it (1 <= j <= count). The number of ways to
        interleave 'j' identical characters into a sequence of length 'k' is C(k + j, j).
        """
        counts = Counter(tiles).values()
        
        # dp[i] will store the number of valid sequences of length i
        dp = [0] * (len(tiles) + 1)
        dp[0] = 1  # Base case: 1 way to form an empty sequence
        
        current_len = 0
        for count in counts:
            # Create a copy for the updated state
            next_dp = list(dp)
            for k in range(current_len + 1):
                if dp[k] == 0:
                    continue
                for j in range(1, count + 1):
                    # math.comb(k + j, j) calculates C(k + j, j)
                    next_dp[k + j] += dp[k] * math.comb(k + j, j)
            
            dp = next_dp
            current_len += count
            
        # Sum of sequences of all lengths from 1 to len(tiles)
        return sum(dp[1:])
