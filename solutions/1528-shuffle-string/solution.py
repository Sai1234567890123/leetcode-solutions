class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        # Since Python strings are immutable, we initialize a list of the same length.
        n = len(s)
        res = [''] * n
        
        # Place each character at its target index.
        for char, target_idx in zip(s, indices):
            res[target_idx] = char
            
        # Join the list into the final restored string.
        return ''.join(res)
