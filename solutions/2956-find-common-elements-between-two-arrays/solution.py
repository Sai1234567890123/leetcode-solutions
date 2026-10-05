class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Convert arrays to hash sets for O(1) average-time membership lookups
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Count elements in nums1 that appear in nums2
        count1 = sum(1 for x in nums1 if x in set2)
        
        # Count elements in nums2 that appear in nums1
        count2 = sum(1 for x in nums2 if x in set1)
        
        return [count1, count2]
