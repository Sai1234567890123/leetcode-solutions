class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        # Get the number of vertices in the graph.
        # The input 'matrix' is an n x n adjacency matrix, so 'n' is its dimension.
        n = len(matrix)
        
        # Initialize an array 'degrees' of size 'n' with all elements set to 0.
        # This array will store the calculated degree for each vertex.
        # degrees[i] will store the degree of vertex 'i'.
        degrees = [0] * n
        
        # Iterate through each vertex 'i' from 0 to n-1.
        # 'i' represents the current vertex whose degree we are calculating.
        for i in range(n):
            # For the current vertex 'i', iterate through all possible other vertices 'j' from 0 to n-1.
            # 'j' represents a potential neighbor of vertex 'i'.
            for j in range(n):
                # In an adjacency matrix, matrix[i][j] = 1 indicates an edge between vertex 'i' and vertex 'j'.
                # If there is an edge, we increment the degree count for vertex 'i'.
                if matrix[i][j] == 1:
                    degrees[i] += 1
                    
        # After iterating through all rows and columns, the 'degrees' array will contain
        # the degree of each vertex from 0 to n-1.
        return degrees
