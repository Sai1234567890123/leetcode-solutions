class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        """
        Determines if x is a Harshad number.
        A Harshad number is divisible by the sum of its digits.
        Returns the digit sum if it is a Harshad number, else -1.
        """
        digit_sum = 0
        temp = x
        
        # Calculate sum of digits mathematically without string conversion
        while temp > 0:
            digit_sum += temp % 10
            temp //= 10
            
        # Check divisibility condition
        if x % digit_sum == 0:
            return digit_sum
        
        return -1
