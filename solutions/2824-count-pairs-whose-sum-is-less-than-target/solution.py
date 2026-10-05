from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Sorting allows us to leverage the two-pointer technique.
        # Order of elements does not matter since we only care about the count of pairs.
        nums.sort()
        
        left = 0
        right = len(nums) - 1
        count = 0
        
        while left < right:
            # If the sum of the smallest and largest available elements is less than target,
            # then nums[left] paired with any element from left + 1 to right will also be < target.
            if nums[left] + nums[right] < target:
                count += (right - left)
                left += 1
            else:
                # Sum is too large, decrement right pointer to reduce the sum
                right -= 1
                
        return count
