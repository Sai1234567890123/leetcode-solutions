class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        # The maximum possible value for a number with `maximumBit` bits is 2^maximumBit - 1.
        # This corresponds to having all of the lowest `maximumBit` bits set to 1.
        max_val = (1 << maximumBit) - 1
        
        # Calculate the cumulative XOR of all elements in nums.
        current_xor = 0
        for num in nums:
            current_xor ^= num
            
        n = len(nums)
        ans = [0] * n
        
        # Process queries from first to last (removing the last element at each step).
        for i in range(n):
            # To maximize (current_xor XOR k), we want (current_xor XOR k) == max_val
            # for the lowest `maximumBit` bits.
            # Using XOR properties: k = current_xor XOR max_val.
            # Note: We take (current_xor & max_val) in case nums contains bits >= maximumBit.
            ans[i] = (current_xor & max_val) ^ max_val
            
            # Remove the last element for the next query by XORing it out.
            current_xor ^= nums[n - 1 - i]
            
        return ans
