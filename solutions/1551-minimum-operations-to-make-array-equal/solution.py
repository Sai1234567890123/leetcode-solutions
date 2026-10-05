class Solution:
    def minOperations(self, n: int) -> int:
        """
        Calculates the minimum number of operations to make all elements equal.
        Each operation shifts 1 from an element > target to an element < target.
        The target element must be the mean of the array, which is n.
        Total operations required simplifies mathematically to n^2 // 4.
        """
        # Alternatively written as (n // 2) * ((n + 1) // 2)
        return (n * n) // 4
