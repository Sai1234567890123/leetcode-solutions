class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        """
        Finds the maximum number of words in a single sentence.
        
        Since words are separated by exactly one space with no leading
        or trailing spaces, the number of words in a sentence is
        equal to (number of spaces) + 1.
        """
        # Using str.count(' ') avoids allocating memory for split lists,
        # running in O(1) auxiliary space and optimal C-level speed.
        return max(s.count(' ') for s in sentences) + 1
