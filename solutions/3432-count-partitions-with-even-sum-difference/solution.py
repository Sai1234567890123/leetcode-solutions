class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        """
        Calculates the number of valid partitions where (left_sum - right_sum) is even.
        
        Mathematical Insight:
        Let S be the total sum of the array.
        For any partition index i, let L = sum(nums[0..i]) and R = sum(nums[i+1..n-1]).
        Since L + R = S, we have R = S - L.
        The difference is: L - R = L - (S - L) = 2 * L - S.
        
        Since 2 * L is always even, the parity of (2 * L - S) depends entirely on S:
        (2 * L - S) % 2 == S % 2.
        
        Therefore:
        - If the total sum S is even, EVERY partition produces an even difference (n - 1 partitions).
        - If the total sum S is odd, NO partition can produce an even difference (0 partitions).
        """
        total_sum = sum(nums)
        return (len(nums) - 1) if total_sum % 2 == 0 else 0
