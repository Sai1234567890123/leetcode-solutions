class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # Convert broken letters to a hash set for O(1) membership lookup.
        broken_set = set(brokenLetters)
        
        # Split the text into individual words.
        words = text.split(' ')
        typed_words_count = 0
        
        for word in words:
            # A word can be typed if none of its characters are in broken_set.
            # Using any() allows short-circuiting on the first broken character encountered.
            if not any(char in broken_set for char in word):
                typed_words_count += 1
                
        return typed_words_count
