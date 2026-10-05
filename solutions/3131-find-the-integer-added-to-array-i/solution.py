class Solution:
    def addedInteger(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Finds the integer x added to every element of nums1 to make it equal to nums2.
        
        Since every element in nums1 is shifted by the exact same value x, 
        the minimum element in nums1 must map to the minimum element in nums2.
        Therefore, x = min(nums2) - min(nums1).
        """
        return min(nums2) - min(nums1)
