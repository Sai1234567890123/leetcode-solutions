class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        # Precompute the index of each character in string s.
        # Since each character appears at most once, a hash map provides O(1) lookups.
        s_indices = {char: idx for idx, char in enumerate(s)}
        
        # Calculate the sum of absolute differences between indices in s and t.
        total_diff = 0
        for idx_t, char in enumerate(t):
            total_diff += abs(s_indices[char] - idx_t)
            
        return total_diff
