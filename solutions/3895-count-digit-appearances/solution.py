class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        target_char = str(digit)
        total_occurrences = 0
        
        # Iterate over each number in nums and count occurrences of target_char
        for num in nums:
            total_occurrences += str(num).count(target_char)
            
        return total_occurrences
