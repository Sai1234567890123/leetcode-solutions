from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans = [0] * n
        # Since numbers are from 1 to n, size n + 1 is sufficient.
        freq = [0] * (n + 1)
        common_count = 0

        for i in range(n):
            # Process element from array A
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                common_count += 1

            # Process element from array B
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                common_count += 1

            ans[i] = common_count

        return ans
