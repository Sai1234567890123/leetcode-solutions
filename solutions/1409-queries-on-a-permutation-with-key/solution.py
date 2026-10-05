class FenwickTree:
    """Binary Indexed Tree (Fenwick Tree) supporting point updates and prefix sum queries."""
    __slots__ = ('tree', 'size')

    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index: int, delta: int) -> None:
        """Adds delta to the element at the given 1-based index."""
        while index <= self.size:
            self.tree[index] += delta
            index += index & (-index)

    def query(self, index: int) -> int:
        """Returns the prefix sum from 1 to index (inclusive)."""
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & (-index)
        return total


class Solution:
    def processQueries(self, queries: list[int], m: int) -> list[int]:
        """
        Processes queries using a Fenwick Tree (Binary Indexed Tree).
        
        Time Complexity: O((m + q) * log(m + q)) where q = len(queries)
        Space Complexity: O(m + q)
        """
        n = len(queries)
        total_size = m + n
        bit = FenwickTree(total_size)
        
        # pos[val] stores the 1-based position of 'val' in the underlying array
        pos = [0] * (m + 1)
        
        # Elements 1 to m are initially placed at indices (n + 1) to (n + m)
        # This leaves n empty slots (1 to n) for moving elements to the front.
        for val in range(1, m + 1):
            curr_pos = n + val
            pos[val] = curr_pos
            bit.update(curr_pos, 1)
            
        result = []
        # curr_front tracks the next available slot for an element moved to the front
        curr_front = n
        
        for q in queries:
            curr_idx = pos[q]
            # The 0-based index in the current permutation is the count of elements
            # strictly before curr_idx.
            result.append(bit.query(curr_idx - 1))
            
            # Remove element from its current position
            bit.update(curr_idx, -1)
            
            # Place element at the new front
            bit.update(curr_front, 1)
            pos[q] = curr_front
            
            curr_front -= 1
            
        return result
