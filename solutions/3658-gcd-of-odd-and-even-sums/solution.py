class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        """
        Computes the greatest common divisor of:
        - sumOdd: the sum of the first n positive odd numbers
        - sumEven: the sum of the first n positive even numbers

        Mathematical derivation:
        1. sumOdd = 1 + 3 + ... + (2n - 1) = n^2
        2. sumEven = 2 + 4 + ... + 2n = n * (n + 1)
        3. gcd(sumOdd, sumEven) = gcd(n^2, n * (n + 1))
                                = n * gcd(n, n + 1)
        Since consecutive integers are coprime, gcd(n, n + 1) = 1.
        Therefore, gcd(n^2, n * (n + 1)) = n * 1 = n.
        """
        return n
