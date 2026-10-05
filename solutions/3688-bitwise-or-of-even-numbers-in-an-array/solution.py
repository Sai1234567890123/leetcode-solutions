class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        result = 0
        
        for num in nums:
            # Check if the number is even using bitwise AND with 1
            if (num & 1) == 0:
                result |= num
                
        return result
