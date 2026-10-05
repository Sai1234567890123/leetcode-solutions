class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        # Construct a bitmask representing the characters present in `allowed`.
        # Each bit from 0 to 25 corresponds to 'a' through 'z'.
        allowed_mask = 0
        for ch in allowed:
            allowed_mask |= 1 << (ord(ch) - ord('a'))
        
        consistent_count = 0
        
        for word in words:
            is_consistent = True
            for ch in word:
                # Check if the bit corresponding to character `ch` is set in allowed_mask.
                if not (allowed_mask & (1 << (ord(ch) - ord('a')))):
                    is_consistent = False
                    break  # Early exit as soon as an invalid character is found
            
            if is_consistent:
                consistent_count += 1
                
        return consistent_count
