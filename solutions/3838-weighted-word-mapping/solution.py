from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        # Pre-compute the character mapping for efficiency and clarity.
        # The problem states: 0 -> 'z', 1 -> 'y', ..., 25 -> 'a'.
        # This means for an index `i`, the character is `chr(ord('z') - i)`.
        # Example:
        # i = 0: chr(ord('z') - 0) = 'z'
        # i = 1: chr(ord('z') - 1) = 'y'
        # i = 25: chr(ord('z') - 25) = 'a'
        char_mapping_table = [chr(ord('z') - i) for i in range(26)]
        
        # Use a list to collect mapped characters, then join them at the end.
        # This is more efficient than repeated string concatenation in Python,
        # which can lead to O(N^2) behavior for N concatenations.
        result_chars = []
        
        # Iterate through each word in the input list.
        for word in words:
            current_word_weight = 0
            # Iterate through each character in the current word.
            for char in word:
                # Calculate the 0-indexed position of the character.
                # 'a' corresponds to index 0, 'b' to 1, ..., 'z' to 25.
                char_index = ord(char) - ord('a')
                
                # Add the corresponding weight from the weights array.
                current_word_weight += weights[char_index]
            
            # Apply modulo 26 to the total word weight.
            # This ensures the result is an index in the range [0, 25].
            mapped_index = current_word_weight % 26
            
            # Look up the mapped character using the pre-computed table.
            mapped_char = char_mapping_table[mapped_index]
            result_chars.append(mapped_char)
            
        # Join all collected characters to form the final result string.
        return "".join(result_chars)
