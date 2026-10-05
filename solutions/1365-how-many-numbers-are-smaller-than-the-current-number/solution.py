class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        # Given constraint: 0 <= nums[i] <= 100
        # We can use a frequency array and prefix sums for O(N + K) optimal time.
        MAX_VAL = 100
        freq = [0] * (MAX_VAL + 1)
        
        # Step 1: Count frequency of each number
        for num in nums:
            freq[num] += 1
            
        # Step 2: Compute running count of strictly smaller numbers
        # smaller_count[i] will store the number of elements strictly less than i
        smaller_count = [0] * (MAX_VAL + 1)
        running_sum = 0
        for i in range(MAX_VAL + 1):
            smaller_count[i] = running_sum
            running_sum += freq[i]
            
        # Step 3: Map each number in the original list to its smaller count
        return [smaller_count[num] for num in nums]
