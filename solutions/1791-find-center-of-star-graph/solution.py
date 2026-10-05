class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        """
        Finds the center node of a valid star graph.
        
        Since a star graph's center node must be connected to every other node,
        it must appear in every edge, including the first two edges.
        """
        u1, v1 = edges[0]
        u2, v2 = edges[1]
        
        # The center node must be common to both edges[0] and edges[1].
        if u1 == u2 or u1 == v2:
            return u1
        return v1
