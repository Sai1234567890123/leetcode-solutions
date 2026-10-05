class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        """
        Finds the number of unique arithmetic triplets (i, j, k) such that
        nums[j] - nums[i] == diff and nums[k] - nums[j] == diff.
        
        Leverages the strictly increasing property of nums using a 3-pointer
        sliding approach to achieve O(n) time and O(1) auxiliary space.
        """
        triplet_count = 0
        i = 0
        j = 0
        n = len(nums)

        # k acts as the rightmost element in the triplet (nums[k])
        for k in range(n):
            # Advance j until nums[k] - nums[j] <= diff
            while j < k and nums[k] - nums[j] > diff:
                j += 1
            
            # If a valid middle element nums[j] is found
            if nums[k] - nums[j] == diff:
                # Advance i until nums[j] - nums[i] <= diff
                while i < j and nums[j] - nums[i] > diff:
                    i += 1
                
                # If a valid leftmost element nums[i] is found
                if nums[j] - nums[i] == diff:
                    triplet_count += 1
                    
        return triplet_count
