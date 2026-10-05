from collections import defaultdict
from math import gcd

class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        """
        Counts pairs (i, j) with 0 <= i < j < n such that:
        nums[i] == nums[j] and (i * j) % k == 0.

        Optimized approach:
        Group indices by their value. For each value, track the frequency
        of gcd(i, k) seen so far. An index j pairs with any previous index i
        if (gcd(i, k) * gcd(j, k)) % k == 0.
        """
        # Group indices by their corresponding value in nums
        val_to_indices = defaultdict(list)
        for i, val in enumerate(nums):
            val_to_indices[val].append(i)

        ans = 0

        # Process each group of identical elements independently
        for indices in val_to_indices.values():
            # If there's only one index, no pairs can be formed
            if len(indices) < 2:
                continue

            # gcd_count maps gcd(i, k) -> frequency of occurrence in the current group
            gcd_count = defaultdict(int)

            for j in indices:
                gcd_j = gcd(j, k)

                # Check all previously observed gcd(i, k)
                for gcd_i, count in gcd_count.items():
                    # (i * j) % k == 0 is equivalent to (gcd(i, k) * gcd(j, k)) % k == 0
                    if (gcd_i * gcd_j) % k == 0:
                        ans += count

                gcd_count[gcd_j] += 1

        return ans
