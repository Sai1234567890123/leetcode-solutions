from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Step 1: Count frequency of each letter in the input string
        counts = Counter(word)
        
        # Step 2: Sort frequencies in descending order to assign the most frequent
        # letters to the keypad slots that require the fewest pushes.
        sorted_freqs = sorted(counts.values(), reverse=True)
        
        total_pushes = 0
        # Step 3: Keys 2 through 9 give us 8 available keys.
        # The first 8 letters require 1 push, the next 8 require 2 pushes, and so on.
        for idx, freq in enumerate(sorted_freqs):
            pushes_per_char = (idx // 8) + 1
            total_pushes += freq * pushes_per_char
            
        return total_pushes
