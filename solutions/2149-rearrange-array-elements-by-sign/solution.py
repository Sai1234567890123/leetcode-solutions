class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        # Pre-allocate output array to avoid repeated append/resize overhead
        result = [0] * n
        
        # Positive integers start at even indices: 0, 2, 4, ...
        # Negative integers start at odd indices: 1, 3, 5, ...
        pos_idx = 0
        neg_idx = 1
        
        # Single pass: place each number into its designated slot preserving relative order
        for num in nums:
            if num > 0:
                result[pos_idx] = num
                pos_idx += 2
            else:
                result[neg_idx] = num
                neg_idx += 2
                
        return result
