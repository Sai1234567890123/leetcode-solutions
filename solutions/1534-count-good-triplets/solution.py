class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0
        
        # Iterate over middle index j and left index i
        for j in range(1, n - 1):
            for i in range(j):
                # Prune early: if |arr[i] - arr[j]| > a, no k can make this triplet valid
                if abs(arr[i] - arr[j]) <= a:
                    val_i = arr[i]
                    val_j = arr[j]
                    for k in range(j + 1, n):
                        val_k = arr[k]
                        if abs(val_j - val_k) <= b and abs(val_i - val_k) <= c:
                            count += 1
                            
        return count
