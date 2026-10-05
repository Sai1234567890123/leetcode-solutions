class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        # Predefined Morse code representations for characters 'a' through 'z'
        morse_table = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", 
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", 
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
        
        # Base ASCII value for 'a' to map characters to morse_table indices
        ord_a = ord('a')
        
        # Use a set to collect distinct transformations
        seen_transformations = set()
        
        for word in words:
            # Map each character to its Morse code and join
            transformation = "".join(morse_table[ord(char) - ord_a] for char in word)
            seen_transformations.add(transformation)
            
        return len(seen_transformations)
