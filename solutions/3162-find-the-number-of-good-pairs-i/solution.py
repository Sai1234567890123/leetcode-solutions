from collections import Counter
from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        Finds the number of good pairs (i, j) such that nums1[i] is divisible by nums2[j] * k.
        Utilizes frequency mapping and sieve/multiple counting to achieve optimal performance,
        scalable to large constraints (LeetCode 3164).
        """
        # Step 1: Pre-filter nums1. Only elements divisible by k can form a valid pair.
        # Store frequency of nums1[i] // k.
        freq1 = Counter()
        for x in nums1:
            if x % k == 0:
                freq1[x // k] += 1
                
        # If no elements in nums1 are divisible by k, no good pairs can exist.
        if not freq1:
            return 0
            
        freq2 = Counter(nums2)
        max_val = max(freq1.keys())
        good_pairs = 0
        
        # Step 2: Iterate over unique values in nums2 and count matching multiples.
        for val, count in freq2.items():
            # Check all multiples of val up to the maximum element in freq1
            for multiple in range(val, max_val + 1, val):
                if multiple in freq1:
                    good_pairs += count * freq1[multiple]
                    
        return good_pairs
