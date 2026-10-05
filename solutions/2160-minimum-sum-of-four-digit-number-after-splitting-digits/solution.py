class Solution:
    def minimumSum(self, num: int) -> int:
        # Extract and sort the 4 digits in ascending order
        digits = sorted(int(d) for d in str(num))
        
        # To minimize the sum of two numbers formed by 4 digits:
        # We must split the digits into two 2-digit numbers.
        # Place the two smallest digits in the tens places,
        # and the remaining two digits in the ones places.
        # new1 = digits[0] * 10 + digits[2]
        # new2 = digits[1] * 10 + digits[3]
        return 10 * (digits[0] + digits[1]) + digits[2] + digits[3]
