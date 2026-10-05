from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # Initialize an empty list to store the indices of words that contain character x.
        result_indices = []
        
        # Iterate through the 'words' array along with their corresponding indices.
        # The 'enumerate' function is used to get both the index (i) and the word itself.
        for i, word in enumerate(words):
            # Check if the character 'x' is present within the current 'word'.
            # Python's 'in' operator for strings efficiently performs this check.
            if x in word:
                # If 'x' is found in the 'word', append its current index to our result list.
                result_indices.append(i)
                
        # After iterating through all words, return the list of collected indices.
        return result_indices
