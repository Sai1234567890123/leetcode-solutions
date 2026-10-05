class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # It is mathematically always possible to construct an array with uniform parity:
        # 1. If all elements in nums1 are even, we can keep nums2[i] = nums1[i] (all even).
        # 2. If all elements in nums1 are odd, we can keep nums2[i] = nums1[i] (all odd).
        # 3. If nums1 contains both even and odd elements:
        #    - There is at least one odd element at some index j.
        #    - For each odd element, set nums2[i] = nums1[i] (odd).
        #    - For each even element at index i, set nums2[i] = nums1[i] - nums1[j] (even - odd = odd).
        #    - Since index i is even and index j is odd, i != j is always satisfied.
        #    - Thus, all elements in nums2 can be made odd.
        # In all possible cases, a valid nums2 can be formed.
        return True
