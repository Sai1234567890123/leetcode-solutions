class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        """
        Counts the number of symmetric integers in the range [low, high].
        An integer is symmetric if it has 2 * n digits and the sum of the
        first n digits equals the sum of the last n digits.
        """
        count = 0
        
        for num in range(low, high + 1):
            s = str(num)
            length = len(s)
            
            # Numbers with an odd number of digits cannot be symmetric
            if length % 2 != 0:
                continue
            
            half = length // 2
            # Compare the sum of the first half of digits with the second half
            left_sum = sum(int(digit) for digit in s[:half])
            right_sum = sum(int(digit) for digit in s[half:])
            
            if left_sum == right_sum:
                count += 1
                
        return count
