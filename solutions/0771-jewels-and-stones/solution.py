class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        Counts how many stones are also jewels using an O(1) lookup hash set.
        """
        # Convert jewels into a set for O(1) average-time membership tests.
        jewel_set = set(jewels)
        
        # Count the number of characters in stones that exist in jewel_set.
        return sum(stone in jewel_set for stone in stones)
