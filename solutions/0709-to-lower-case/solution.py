class Solution:
    def toLowerCase(self, s: str) -> str:
        """
        Converts uppercase ASCII letters in a string to lowercase 
        without relying on built-in conversion functions like s.lower().
        """
        result = []
        for char in s:
            # Check if the character is an uppercase ASCII letter ('A' to 'Z')
            if 'A' <= char <= 'Z':
                # In ASCII, the difference between lowercase and uppercase is 32.
                # Alternatively, bitwise OR with 32 (0b00100000) sets the 6th bit.
                result.append(chr(ord(char) | 32))
            else:
                result.append(char)
                
        return "".join(result)
