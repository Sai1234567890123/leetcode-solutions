class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        """
        Concatenates the input list `nums` with itself.
        
        In Python, list multiplication (`nums * 2`) or concatenation (`nums + nums`)
        is implemented at the C-level (CPython `list_repeat`), allocating memory
        in a single block and performing a fast memory copy (memcpy).
        """
        return nums + nums
