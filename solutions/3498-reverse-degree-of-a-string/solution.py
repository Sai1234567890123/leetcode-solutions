class Solution:
    def reverseDegree(self, s: str) -> int:
        total_reverse_degree = 0  # Initialize the sum for the reverse degree

        # Iterate through the string with both the 0-indexed position (i) and the character (char).
        # For example, for "abc":
        # i=0, char='a'
        # i=1, char='b'
        # i=2, char='c'
        for i, char in enumerate(s):
            # Calculate the 0-indexed position of the character in the standard alphabet.
            # 'a' -> 0, 'b' -> 1, ..., 'z' -> 25
            # This is done by subtracting the ASCII value of 'a' from the character's ASCII value.
            standard_alphabet_pos_0_indexed = ord(char) - ord('a')

            # Calculate the position in the reversed alphabet.
            # 'a' -> 26, 'b' -> 25, ..., 'z' -> 1
            # The formula is 26 - (0-indexed standard position).
            reversed_alphabet_pos = 26 - standard_alphabet_pos_0_indexed

            # Calculate the 1-indexed position of the character in the string.
            # If 'i' is the 0-indexed position, the 1-indexed position is 'i + 1'.
            string_pos_1_indexed = i + 1

            # Multiply the reversed alphabet position by the 1-indexed string position
            # and add the product to the total sum.
            total_reverse_degree += reversed_alphabet_pos * string_pos_1_indexed

        return total_reverse_degree
