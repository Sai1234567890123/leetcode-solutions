class Solution:
    def sumOfMultiples(self, n: int) -> int:
        """
        Calculates the sum of all integers in [1, n] divisible by 3, 5, or 7
        using the Principle of Inclusion-Exclusion (PIE) in O(1) time and space.
        """
        def sum_multiples_of(k: int) -> int:
            # Number of multiples of k in the range [1, n]
            m = n // k
            # Sum of arithmetic progression: k * (1 + 2 + ... + m) = k * m * (m + 1) // 2
            return k * m * (m + 1) // 2

        # 3, 5, and 7 are pairwise coprime, so:
        # lcm(3, 5) = 15, lcm(3, 7) = 21, lcm(5, 7) = 35, lcm(3, 5, 7) = 105
        return (
            sum_multiples_of(3)
            + sum_multiples_of(5)
            + sum_multiples_of(7)
            - sum_multiples_of(15)
            - sum_multiples_of(21)
            - sum_multiples_of(35)
            + sum_multiples_of(105)
        )
