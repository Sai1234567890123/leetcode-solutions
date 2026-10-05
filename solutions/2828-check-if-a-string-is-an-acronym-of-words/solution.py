class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        # Fast exit: if lengths differ, s cannot be an acronym of words
        if len(words) != len(s):
            return False
        
        # Check if the first character of each word matches the corresponding character in s
        return all(word[0] == char for word, char in zip(words, s))
