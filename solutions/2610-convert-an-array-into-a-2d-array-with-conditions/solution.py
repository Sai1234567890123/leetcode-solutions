class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        """
        Creates a 2D array from nums with minimal rows such that each row contains distinct integers.
        """
        # Frequency map or array to track how many times each number has appeared.
        # Since nums[i] <= len(nums), a fixed-size array or hash map can be used.
        freq: dict[int, int] = {}
        res: list[list[int]] = []

        for num in nums:
            # The current count indicates the 0-indexed row where this instance belongs.
            count = freq.get(num, 0)
            
            # If the row doesn't exist yet, create a new row.
            if count == len(res):
                res.append([])
            
            # Place the number into its assigned row and increment frequency.
            res[count].append(num)
            freq[num] = count + 1

        return res
