from collections import defaultdict

class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        """
        Counts the number of pairs (i, j) with i < j such that |nums[i] - nums[j]| == k.
        
        Uses a single-pass hash map approach similar to Two Sum.
        Time Complexity: O(N)
        Space Complexity: O(min(N, M)) where M is the range of values in nums.
        """
        freq = defaultdict(int)
        pair_count = 0
        
        for num in nums:
            # Check how many previous numbers satisfy |num - prev| == k
            # That is, prev == num - k or prev == num + k
            pair_count += freq[num - k] + freq[num + k]
            
            # Record current number's frequency for future pairs
            freq[num] += 1
            
        return pair_count
