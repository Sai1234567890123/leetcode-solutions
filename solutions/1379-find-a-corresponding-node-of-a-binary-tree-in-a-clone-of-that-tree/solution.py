from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        """
        Traverses both trees simultaneously to find the target node by reference.
        Using BFS ensures we avoid recursion depth limits in Python (since N <= 10^4).
        Comparing node references (original_node is target) directly answers both
        the base problem and the follow-up where node values can be duplicated.
        """
        if not original or not cloned:
            return None
        
        # Queue stores pairs of (original_node, cloned_node)
        queue = deque([(original, cloned)])
        
        while queue:
            orig_node, clone_node = queue.popleft()
            
            # Check reference identity, not value equality
            if orig_node is target:
                return clone_node
            
            if orig_node.left:
                queue.append((orig_node.left, clone_node.left))
            if orig_node.right:
                queue.append((orig_node.right, clone_node.right))
                
        return None
