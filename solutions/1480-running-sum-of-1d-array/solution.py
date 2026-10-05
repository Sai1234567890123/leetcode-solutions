class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        # Perform in-place prefix accumulation to achieve O(1) auxiliary space.
        # nums[i] becomes the sum of all elements from index 0 to i.
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        return nums
