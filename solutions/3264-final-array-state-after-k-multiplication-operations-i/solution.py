import heapq
from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        """
        Simulates k operations where each operation multiplies the minimum element
        (breaking ties by smallest index) by `multiplier`.
        """
        # If multiplier is 1 or no operations, the array remains unchanged.
        if multiplier == 1 or k == 0:
            return nums
        
        # Build a min-heap storing tuples of (value, index).
        # Python's tuple comparison naturally breaks ties using the second element (index).
        heap = [(val, idx) for idx, val in enumerate(nums)]
        heapq.heapify(heap)
        
        # Perform k operations
        for _ in range(k):
            val, idx = heap[0]
            new_val = val * multiplier
            # heapreplace pops the smallest item and pushes the new item efficiently
            heapq.heapreplace(heap, (new_val, idx))
            nums[idx] = new_val
            
        return nums
