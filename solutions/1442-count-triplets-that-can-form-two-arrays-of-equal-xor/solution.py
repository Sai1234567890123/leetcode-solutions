from collections import defaultdict

class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        """
        Calculates the number of triplets (i, j, k) with 0 <= i < j <= k < len(arr)
        such that XOR(arr[i...j-1]) == XOR(arr[j...k]).
        
        Key Insight:
            XOR(arr[i...j-1]) == XOR(arr[j...k]) 
            <=> XOR(arr[i...k]) == 0
            <=> prefix_xor[i] == prefix_xor[k + 1]
            
        For any such pair (i, k), any j strictly between i and k (i < j <= k)
        forms a valid triplet. There are (k - i) choices for j.
        """
        # count_map[val] stores the frequency of prefix XOR value `val`
        count_map = defaultdict(int)
        # total_idx_map[val] stores the sum of indices where prefix XOR value `val` occurred
        total_idx_map = defaultdict(int)
        
        # Base case: prefix XOR before any element (index 0) is 0
        count_map[0] = 1
        total_idx_map[0] = 0
        
        prefix = 0
        ans = 0
        
        # m represents (k + 1), ranging from 1 to len(arr)
        for m, num in enumerate(arr, start=1):
            prefix ^= num
            
            # If `prefix` has appeared before at indices i_1, i_2, ..., i_c:
            # Each gives (m - 1 - i) valid triplets for this (m - 1) as k.
            # Total for this m = sum((m - 1) - i) = c * (m - 1) - sum(i)
            if prefix in count_map:
                c = count_map[prefix]
                sum_i = total_idx_map[prefix]
                ans += c * (m - 1) - sum_i
            
            # Update prefix XOR tracking
            count_map[prefix] += 1
            total_idx_map[prefix] += m
            
        return ans
