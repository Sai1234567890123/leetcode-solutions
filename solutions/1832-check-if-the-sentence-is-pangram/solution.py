class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # A pangram must contain at least 26 characters.
        if len(sentence) < 26:
            return False

        # Bitmask to track seen characters ('a' -> bit 0, 'z' -> bit 25).
        # Target mask has all first 26 bits set: (1 << 26) - 1.
        seen_mask = 0
        target_mask = (1 << 26) - 1

        for char in sentence:
            # Map 'a'..'z' to 0..25 and set the corresponding bit
            seen_mask |= 1 << (ord(char) - ord('a'))
            
            # Early exit: if all 26 letters have been encountered, terminate early
            if seen_mask == target_mask:
                return True

        return seen_mask == target_mask
