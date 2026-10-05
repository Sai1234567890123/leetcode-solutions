class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Find the index of the first occurrence of ch
        idx = word.find(ch)
        
        # If ch is not found, return the original word unchanged
        if idx == -1:
            return word
            
        # Reverse the prefix from index 0 to idx (inclusive), then append the remainder
        return word[:idx + 1][::-1] + word[idx + 1:]
