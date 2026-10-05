from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        # Define the set of vowels for O(1) membership check
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Count frequency of each character in s
        freq = Counter(s)
        
        max_vowel_freq = 0
        max_consonant_freq = 0
        
        # Find maximum frequency among vowels and consonants
        for char, count in freq.items():
            if char in vowels:
                if count > max_vowel_freq:
                    max_vowel_freq = count
            else:
                if count > max_consonant_freq:
                    max_consonant_freq = count
                    
        return max_vowel_freq + max_consonant_freq
