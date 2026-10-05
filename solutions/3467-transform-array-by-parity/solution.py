class Solution:
    def transformArray(self, nums: list[int]) -> list[int]:
        # Count the number of even integers in the input array.
        # Since even numbers map to 0 and odd numbers map to 1,
        # sorting them simply places all 0s before all 1s.
        even_count = sum(1 for x in nums if x % 2 == 0)
        odd_count = len(nums) - even_count
        
        # Construct and return the result: all zeros followed by all ones.
        return [0] * even_count + [1] * odd_count
