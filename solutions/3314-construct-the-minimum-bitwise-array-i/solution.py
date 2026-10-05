class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        ans = []
        for x in nums:
            if x == 2:
                # 2 is the only even prime. For any integer k, k OR (k + 1) is always odd.
                ans.append(-1)
            else:
                # Find the lowest unset bit of x: (x + 1) & -(x + 1) gives 2^k,
                # where bits 0 to k - 1 of x are all 1s.
                # To minimize the answer, we flip the most significant bit among these
                # trailing ones, which is bit (k - 1) (i.e. value 2^(k - 1)).
                lowest_unset_bit = (x + 1) & -(x + 1)
                ans.append(x - (lowest_unset_bit >> 1))
        return ans
