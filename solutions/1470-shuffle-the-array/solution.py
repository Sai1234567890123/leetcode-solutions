class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        # Preallocate the result array to avoid dynamic resizing overhead
        result = [0] * (2 * n)
        
        # Interleave elements: x_i goes to 2*i, y_i goes to 2*i + 1
        for i in range(n):
            result[2 * i] = nums[i]
            result[2 * i + 1] = nums[i + n]
            
        return result
