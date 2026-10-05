class Solution:
    def sortSentence(self, s: str) -> str:
        # Split the shuffled sentence into individual word-number tokens
        words = s.split()
        
        # Preallocate a list to place words directly into their correct 0-indexed positions
        n = len(words)
        reconstructed = [None] * n
        
        for word in words:
            # The last character represents the 1-indexed position
            pos = int(word[-1]) - 1
            # The actual word content excludes the trailing numeric digit
            reconstructed[pos] = word[:-1]
            
        # Join the sorted words with single spaces
        return " ".join(reconstructed)
