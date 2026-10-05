class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        # Using the property of XOR:
        # If pref[i] = pref[i - 1] ^ arr[i], then arr[i] = pref[i - 1] ^ pref[i].
        # We iterate backwards to modify the array in-place, achieving O(1) auxiliary space.
        for i in range(len(pref) - 1, 0, -1):
            pref[i] ^= pref[i - 1]
            
        return pref
