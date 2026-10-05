class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Calculate the sum of all integers from 1 to n.
        # This is the sum of an arithmetic series: n * (n + 1) / 2.
        # Using integer division (//) as all sums will be integers.
        total_sum_up_to_n = n * (n + 1) // 2

        # Calculate num2: the sum of all integers in the range [1, n] that are divisible by m.
        # These numbers are m, 2*m, 3*m, ..., k*m, where k*m <= n.
        # The largest multiple of m less than or equal to n is found by k = n // m.
        # The sum of these multiples is m * (1 + 2 + ... + k).
        # The sum 1 + 2 + ... + k is another arithmetic series: k * (k + 1) / 2.
        
        # k represents how many multiples of m are there up to n.
        k = n // m 
        
        # num2 is the sum of these multiples.
        sum_divisible_by_m = m * (k * (k + 1) // 2)

        # We need to find num1 - num2.
        # We know that:
        # (sum of all integers from 1 to n) = num1 + num2
        # So, total_sum_up_to_n = num1 + num2
        # This implies num1 = total_sum_up_to_n - num2.
        
        # Substituting num1 into the expression we need to return:
        # num1 - num2 = (total_sum_up_to_n - num2) - num2
        #             = total_sum_up_to_n - 2 * num2
        
        return total_sum_up_to_n - 2 * sum_divisible_by_m
