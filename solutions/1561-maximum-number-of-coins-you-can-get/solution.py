class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        """
        Greedy strategy:
        To maximize our share, we want Bob to take the smallest possible piles.
        For each round of 3 piles, Alice takes the largest remaining, we take the
        second largest remaining, and Bob takes the smallest remaining pile.
        
        Given 3n piles:
        - Bob gets the smallest n piles.
        - Out of the remaining 2n largest piles, Alice and we alternate picking 
          from the top.
        - Therefore, we receive elements at indices: n, n + 2, n + 4, ..., 3n - 2.
        """
        piles.sort()
        n = len(piles) // 3
        # piles[n::2] selects every second element starting from index n up to the end.
        return sum(piles[n::2])
