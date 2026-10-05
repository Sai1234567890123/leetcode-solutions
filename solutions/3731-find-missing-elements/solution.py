from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        """
        Finds all missing integers between min(nums) and max(nums) in sorted order.
        
        Time Complexity: O(N log N + M) where N = len(nums), M = number of missing elements.
        Auxiliary Space Complexity: O(1) beyond sorting overhead and the returned result.
        """
        # Sort the array to process elements in increasing order
        nums.sort()
        
        missing = []
        
        # Traverse adjacent elements and collect integers in gaps
        for i in range(len(nums) - 1):
            # For any gap between nums[i] and nums[i + 1], append all missing values
            for val in range(nums[i] + 1, nums[i + 1]):
                missing.append(val)
                
        return missing
