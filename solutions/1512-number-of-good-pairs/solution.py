from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        """
        Calculates the number of good pairs (i, j) where nums[i] == nums[j] and i < j.
        """
        count_map = defaultdict(int)
        good_pairs = 0
        
        for num in nums:
            # Each time we encounter `num`, it forms a good pair with every
            # occurrence of `num` seen previously.
            good_pairs += count_map[num]
            count_map[num] += 1
            
        return good_pairs
