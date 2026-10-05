class Solution:
    def scoreOfString(self, s: str) -> int:
        total_score = 0  # Initialize the total score to accumulate differences.
        
        # Iterate through the string from the first character up to the second-to-last character.
        # This ensures that for each index 'i', 's[i+1]' is a valid index,
        # allowing us to consider all adjacent pairs (s[i], s[i+1]).
        # The loop will run 'len(s) - 1' times, covering all adjacent pairs.
        for i in range(len(s) - 1):
            # Get the ASCII (or Unicode) value of the current character s[i].
            # Python's ord() function returns the Unicode code point, which
            # is equivalent to ASCII for ASCII characters.
            char1_ascii = ord(s[i])
            
            # Get the ASCII (or Unicode) value of the next character s[i+1].
            char2_ascii = ord(s[i+1])
            
            # Calculate the absolute difference between their ASCII values
            # and add this difference to the total score.
            total_score += abs(char1_ascii - char2_ascii)
            
        return total_score
