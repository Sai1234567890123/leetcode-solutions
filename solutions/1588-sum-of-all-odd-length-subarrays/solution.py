class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        """
        Calculates the sum of all odd-length subarrays in O(n) time and O(1) auxiliary space
        by counting the contribution of each element arr[i] across all valid subarrays.
        """
        n = len(arr)
        total_sum = 0
        
        for i in range(n):
            # Total subarrays containing arr[i]:
            # Number of valid starting positions: (i + 1) (from index 0 to i)
            # Number of valid ending positions: (n - i) (from index i to n - 1)
            total_subarrays = (i + 1) * (n - i)
            
            # Subarrays of odd length have start and end indices of the same parity.
            # Exactly ceil(total_subarrays / 2) = (total_subarrays + 1) // 2 of these
            # subarrays will have an odd length.
            odd_subarrays_count = (total_subarrays + 1) // 2
            
            # Contribution of arr[i] to the total sum
            total_sum += odd_subarrays_count * arr[i]
            
        return total_sum
