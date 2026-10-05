class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        """
        Creates the target array by inserting each element from `nums`
        at the specified index in `index`.
        """
        target = []
        
        # Iterate through pairs of (val, idx) and insert sequentially
        for val, idx in zip(nums, index):
            target.insert(idx, val)
            
        return target
