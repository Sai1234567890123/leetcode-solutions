class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        """
        Calculates the difference between the product and sum of the digits of n.
        Uses arithmetic operations to achieve O(1) auxiliary space without string conversion.
        """
        digit_product = 1
        digit_sum = 0
        
        while n > 0:
            # Extract the least significant digit
            digit = n % 10
            digit_product *= digit
            digit_sum += digit
            # Remove the least significant digit
            n //= 10
            
        return digit_product - digit_sum
