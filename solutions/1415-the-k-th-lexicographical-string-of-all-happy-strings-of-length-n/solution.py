class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Total number of happy strings of length n is 3 * 2^(n - 1)
        total_strings = 3 * (1 << (n - 1))
        
        # If k exceeds the total possible happy strings, return ""
        if k > total_strings:
            return ""
        
        # Convert k to 0-indexed for easier partition arithmetic
        k -= 1
        
        result = []
        
        # Determine the first character:
        # Each first character ('a', 'b', 'c') roots a subtree of size 2^(n - 1)
        block_size = 1 << (n - 1)
        first_char_index = k // block_size
        result.append(['a', 'b', 'c'][first_char_index])
        k %= block_size
        
        # Determine the remaining n - 1 characters
        # At each step, there are 2 choices (excluding the immediately preceding character)
        for i in range(1, n):
            block_size >>= 1
            choice_index = k // block_size
            k %= block_size
            
            # The two candidate characters in lexicographical order
            prev_char = result[-1]
            candidates = [ch for ch in ['a', 'b', 'c'] if ch != prev_char]
            
            result.append(candidates[choice_index])
            
        return "".join(result)
