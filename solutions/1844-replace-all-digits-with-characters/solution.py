class Solution:
    def replaceDigits(self, s: str) -> str:
        # Convert string to a mutable list of characters
        res = list(s)
        
        # Iterate over all odd indices
        for i in range(1, len(res), 2):
            # Shift the preceding character by the digit value at the current index
            res[i] = chr(ord(res[i - 1]) + int(res[i]))
            
        return "".join(res)
