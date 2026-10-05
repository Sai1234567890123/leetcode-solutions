class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        decompressed: list[int] = []
        
        # Iterate through nums in pairs: (freq, val) at indices (i, i + 1)
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i + 1]
            # [val] * freq creates the repeated sequence in C-speed,
            # and extend appends the elements in-place to avoid reallocating intermediate lists.
            decompressed.extend([val] * freq)
            
        return decompressed
