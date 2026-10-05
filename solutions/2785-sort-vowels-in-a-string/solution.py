class Solution:
    def sortVowels(self, s: str) -> str:
        # Vowels ordered by their ASCII values:
        # 'A' (65) < 'E' (69) < 'I' (73) < 'O' (79) < 'U' (85) <
        # 'a' (97) < 'e' (101) < 'i' (105) < 'o' (111) < 'u' (117)
        VOWELS_SORTED = "AEIOUaeiou"
        vowel_set = set(VOWELS_SORTED)
        
        # Count frequency of each vowel in s (Counting Sort approach: O(1) auxiliary space)
        vowel_counts = [0] * len(VOWELS_SORTED)
        vowel_to_idx = {char: i for i, char in enumerate(VOWELS_SORTED)}
        
        for ch in s:
            if ch in vowel_set:
                vowel_counts[vowel_to_idx[ch]] += 1
        
        # Reconstruct the string: preserve consonants, place vowels in ASCII order
        result = list(s)
        current_vowel_idx = 0
        
        for i, ch in enumerate(result):
            if ch in vowel_set:
                # Advance to the next available vowel in ASCII order
                while vowel_counts[current_vowel_idx] == 0:
                    current_vowel_idx += 1
                
                result[i] = VOWELS_SORTED[current_vowel_idx]
                vowel_counts[current_vowel_idx] -= 1
                
        return "".join(result)
