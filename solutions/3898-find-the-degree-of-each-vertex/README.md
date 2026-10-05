# 3898. Find the Degree of Each Vertex

**Difficulty:** Easy  
**LeetCode Link:** [https://leetcode.com/problems/find-the-degree-of-each-vertex/](https://leetcode.com/problems/find-the-degree-of-each-vertex/)  
**Topics:** Array, Graph Theory, Matrix

---

## 📝 Problem Statement

You are given a 2D integer array `matrix` of size `n x n` representing the adjacency matrix of an undirected graph with `n` vertices labeled from 0 to `n - 1`.

	- `matrix[i][j] = 1` indicates that there is an edge between vertices `i` and `j`.

	- `matrix[i][j] = 0` indicates that there is no edge between vertices `i` and `j`.

The **degree** of a vertex is the number of edges connected to it.

Return an integer array `ans` of size `n` where `ans[i]` represents the degree of vertex `i`.

 
Example 1:

**Input:** matrix = [[0,1,1],[1,0,1],[1,1,0]]

**Output:** [2,2,2]

**Explanation:**

	- Vertex 0 is connected to vertices 1 and 2, so its degree is 2.

	- Vertex 1 is connected to vertices 0 and 2, so its degree is 2.

	- Vertex 2 is connected to vertices 0 and 1, so its degree is 2.

Thus, the answer is `[2, 2, 2]`.

Example 2:

**Input:** matrix = [[0,1,0],[1,0,0],[0,0,0]]

**Output:** [1,1,0]

**Explanation:**

	- Vertex 0 is connected to vertex 1, so its degree is 1.

	- Vertex 1 is connected to vertex 0, so its degree is 1.

	- Vertex 2 is not connected to any vertex, so its degree is 0.

Thus, the answer is `[1, 1, 0]`.

Example 3:

**Input:** matrix = [[0]]

**Output:** [0]

**Explanation:**

There is only one vertex and it has no edges connected to it. Thus, the answer is [0].

 
**Constraints:**

	- `1

---

## 💻 Implementation (python3)

```py
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
```

---

## 💡 Solution, Complexity & Interview Analysis

## Intuition & Thought Process

The problem asks us to find the degree of each vertex in an undirected graph represented by an adjacency matrix. The degree of a vertex is defined as the number of edges connected to it.

In an adjacency matrix `matrix`, `matrix[i][j] = 1` signifies that there is an edge between vertex `i` and vertex `j`. Conversely, `matrix[i][j] = 0` means there is no edge. Since the graph is undirected, `matrix[i][j]` will always be equal to `matrix[j][i]`.

To find the degree of a specific vertex `i`, we simply need to count how many `1`s are present in its corresponding row (or column) in the adjacency matrix. Each `1` in `matrix[i][j]` (for a fixed `i` and varying `j`) indicates an edge connecting vertex `i` to vertex `j`. Summing these `1`s directly gives us the total number of edges connected to vertex `i`, which is its degree.

For example, if we want to find the degree of vertex `0`, we would look at `matrix[0][0]`, `matrix[0][1]`, `matrix[0][2]`, ..., `matrix[0][n-1]`. Each `1` in this row contributes one to the degree of vertex `0`.

## Step-by-Step Approach

1.  **Determine `n`**: First, get the number of vertices `n` from the input `matrix`. Since it's an `n x n` matrix, `n` is simply `len(matrix)`.
2.  **Initialize `degrees` array**: Create an array, let's call it `degrees`, of size `n`. Initialize all its elements to `0`. `degrees[i]` will eventually store the degree of vertex `i`.
3.  **Iterate through vertices**: Loop through each vertex `i` from `0` to `n-1`. This outer loop processes each vertex one by one to calculate its degree.
4.  **Iterate through potential neighbors**: Inside the outer loop, for each vertex `i`, loop through all other possible vertices `j` from `0` to `n-1`. This inner loop checks for edges connecting `i` to any other vertex `j`.
5.  **Count edges**: Inside the inner loop, check the value of `matrix[i][j]`. If `matrix[i][j]` is `1`, it means an edge exists between `i` and `j`. Increment `degrees[i]` by `1`.
6.  **Return result**: After the loops complete, the `degrees` array will contain the degree of every vertex. Return this array.

## Complexity Analysis

*   **Time Complexity: O(n^2)**
    *   We have a nested loop structure. The outer loop iterates `n` times (for each vertex `i`).
    *   The inner loop also iterates `n` times (for each potential neighbor `j`).
    *   Inside the inner loop, operations like array access and increment are constant time (O(1)).
    *   Therefore, the total number of operations is proportional to `n * n = n^2`.
    *   Given `n <= 100`, `n^2` is at most `100^2 = 10,000`, which is very efficient and well within typical time limits.

*   **Space Complexity: O(n)**
    *   We create an additional array `degrees` of size `n` to store the results.
    *   This array's size scales linearly with the number of vertices `n`.
    *   No other data structures that scale with `n` or `n^2` are used.

## Common Pitfalls / Mistakes

1.  **Misinterpreting `matrix[i][j]`**: Some candidates might incorrectly assume `matrix[i][j]` could represent something other than a simple edge presence (e.g., edge weight, or count of parallel edges). The problem explicitly states `1` for an edge and `0` for no edge.
2.  **Handling self-loops**: In standard graph theory, a self-loop (an edge from a vertex to itself) contributes 2 to the degree of that vertex. However, adjacency matrices for simple graphs (which this problem implies by `matrix[i][i]=0` in examples) typically do not have self-loops, or if they did, `matrix[i][i]` would be 1 and counted once. The problem examples show `matrix[i][i]=0`, so simply summing `1`s in the row is correct.
3.  **Confusing directed vs. undirected**: If the graph were directed, `matrix[i][j]` would represent an edge from `i` to `j`. The "out-degree" of `i` would be the sum of its row, and the "in-degree" of `i` would be the sum of its column. Since the problem specifies an *undirected* graph, the row sum (or column sum) correctly gives the total degree.
4.  **Off-by-one errors**: While Python's `range(n)` naturally handles `0` to `n-1`, in languages where loop bounds are manually managed, forgetting to iterate up to `n-1` or `n` can lead to incorrect results or out-of-bounds errors.

## Real Interview Follow-Up Questions

1.  **What if the graph was represented by an adjacency list instead of an adjacency matrix? How would you find the degrees?**
    *   **Answer:** If the graph is represented by an adjacency list, say `adj_list`, where `adj_list[i]` is a list of neighbors of vertex `i`, then the degree of vertex `i` is simply the number of elements in `adj_list[i]`.
    *   **Time Complexity:** O(V) (where V is the number of vertices). We iterate through each vertex once and get the length of its corresponding list, which is an O(1) operation.
    *   **Space Complexity:** O(V+E) for the adjacency list itself (where E is the number of edges), plus O(V) for the degrees array. This is generally more space-efficient for sparse graphs (graphs with relatively few edges compared to `V^2`).

2.  **What if `n` was very large (e.g., 10^5 or 10^6)? Would your current solution still be optimal?**
    *   **Answer:** For `n = 10^5`, an O(n^2) solution would involve `(10^5)^2 = 10^10` operations, which is far too slow for typical time limits (usually around `10^8` operations per second).
    *   Furthermore, an adjacency matrix for `n = 10^5` would require `(10^5)^2` memory cells. If each cell stores an integer, this would be `10^10` integers, which is terabytes of memory, making the matrix representation itself infeasible.
    *   In such large-scale scenarios, an adjacency list representation would be mandatory, especially if the graph is sparse. As discussed above, finding degrees from an adjacency list is O(V), which would be `10^5` operations – perfectly feasible.

3.  **How would you handle weighted graphs if the problem asked for the sum of weights connected to each vertex?**
    *   **Answer:** If `matrix[i][j]` stored the weight of the edge between `i` and `j` (and `0` if no edge), and we needed the sum of weights, we would change the logic slightly. Instead of `if matrix[i][j] == 1: degrees[i] += 1`, we would use `degrees[i] += matrix[i][j]`. This would sum the weights of all edges connected to vertex `i`. The time and space complexity would remain O(n^2) and O(n) respectively.

4.  **What if the graph could have parallel edges (multiple edges between the same two vertices)?**
    *   **Answer:** A standard adjacency matrix typically cannot represent parallel edges directly, as `matrix[i][j]` can only hold one value. If parallel edges were allowed, the `matrix[i][j]` entry would usually store the *count* of edges between `i` and `j`. In that case, to find the degree of vertex `i`, we would sum `matrix[i][j]` for all `j`. Our current code's `if matrix[i][j] == 1: degrees[i] += 1` would need to be modified to `degrees[i] += matrix[i][j]` to correctly count all parallel edges.

5.  **What if the graph was directed? How would you find the in-degree and out-degree for each vertex?**
    *   **Answer:** For a directed graph, we distinguish between "in-degree" (number of incoming edges) and "out-degree" (number of outgoing edges).
        *   **Out-degree of vertex `i`**: This would be the sum of `1`s in row `i` of the adjacency matrix (`sum(matrix[i][j] for j in range(n))`). Our current solution effectively calculates out-degrees.
        *   **In-degree of vertex `i`**: This would be the sum of `1`s in column `i` of the adjacency matrix (`sum(matrix[j][i] for j in range(n))`).
    *   To calculate both, we would need two arrays (e.g., `in_degrees` and `out_degrees`) or an array of tuples. The time complexity would still be O(n^2) to iterate through the matrix, and space complexity O(n) for each degree array.
