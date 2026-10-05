from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        """
        Distributes elements of nums into two arrays arr1 and arr2 based on
        the comparison between their last elements, and returns arr1 + arr2.
        """
        # Step 1: Initialize arr1 and arr2 with the first two elements.
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        
        # Step 2: Iterate through the remaining elements and distribute accordingly.
        for num in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(num)
            else:
                arr2.append(num)
                
        # Step 3: Concatenate and return the combined list.
        return arr1 + arr2
