class FindElements:

    def __init__(self, root: TreeNode | None):
        """
        Recovers the contaminated tree and indexes all existing values.
        Time Complexity: O(N) where N is the number of nodes in the tree.
        Space Complexity: O(N) to store values in a hash set.
        """
        self.seen: set[int] = set()
        
        if root is not None:
            root.val = 0
            self._recover(root)

    def _recover(self, node: TreeNode) -> None:
        """
        DFS traversal to restore node values and populate the lookup set.
        """
        self.seen.add(node.val)
        
        if node.left is not None:
            node.left.val = 2 * node.val + 1
            self._recover(node.left)
            
        if node.right is not None:
            node.right.val = 2 * node.val + 2
            self._recover(node.right)

    def find(self, target: int) -> bool:
        """
        Checks if the target value exists in the recovered binary tree.
        Time Complexity: O(1) average.
        Space Complexity: O(1).
        """
        return target in self.seen
