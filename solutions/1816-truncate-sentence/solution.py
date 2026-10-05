class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        """
        Truncates the sentence to only the first k words.
        
        Since words are separated by exactly one space, the k-th word ends
        immediately before the k-th space character.
        """
        space_count = 0
        for i, char in enumerate(s):
            if char == ' ':
                space_count += 1
                # When we reach the k-th space, the first k words have ended
                if space_count == k:
                    return s[:i]
        
        # If the string contains fewer than or exactly k spaces, return s
        return s
