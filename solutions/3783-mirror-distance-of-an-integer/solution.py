class Solution:
    def mirrorDistance(self, n: int) -> int:
        # Store the original value of n, as n will be modified during the reversal process.
        original_n = n
        
        reversed_n = 0
        # Iterate through the digits of n to reverse it.
        # This loop continues as long as there are digits left in n.
        while n > 0:
            # Get the last digit of n using the modulo operator.
            digit = n % 10
            
            # Build the reversed number:
            # 1. Multiply reversed_n by 10 to shift its existing digits one position to the left.
            # 2. Add the current 'digit' to the rightmost position.
            reversed_n = reversed_n * 10 + digit
            
            # Remove the last digit from n by performing integer division.
            n //= 10
            
        # The mirror distance is defined as the absolute difference between the original number
        # and its reversed version.
        return abs(original_n - reversed_n)
