class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        # Sort the array in non-decreasing order.
        # This allows us to access the smallest elements sequentially.
        nums.sort()
        
        # In each round, Alice picks nums[i] and Bob picks nums[i + 1].
        # Bob appends first, followed by Alice, effectively swapping their positions.
        for i in range(0, len(nums), 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            
        return nums
