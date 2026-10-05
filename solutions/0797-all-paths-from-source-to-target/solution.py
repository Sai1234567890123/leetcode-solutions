class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        """
        Finds all paths from node 0 to node n - 1 in a directed acyclic graph (DAG).
        Uses backtracking / DFS traversal.
        """
        target = len(graph) - 1
        result: list[list[int]] = []
        path: list[int] = [0]

        def dfs(curr: int) -> None:
            # Base case: reached the destination node
            if curr == target:
                # Append a shallow copy of the current valid path
                result.append(list(path))
                return

            # Explore all outgoing edges from the current node
            for neighbor in graph[curr]:
                path.append(neighbor)
                dfs(neighbor)
                # Backtrack to explore alternative branches
                path.pop()

        dfs(0)
        return result
