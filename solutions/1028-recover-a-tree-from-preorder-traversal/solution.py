# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode | None:
        stack: list[TreeNode] = []
        i = 0
        n = len(traversal)
        
        while i < n:
            # Step 1: Count the number of dashes to determine depth
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1
            
            # Step 2: Parse the node's integer value
            val = 0
            while i < n and traversal[i].isdigit():
                val = val * 10 + int(traversal[i])
                i += 1
            
            node = TreeNode(val)
            
            # Step 3: Maintain the stack such that stack size matches current depth
            # The node at stack[depth - 1] must be the parent of the current node
            while len(stack) > depth:
                stack.pop()
            
            # Step 4: Attach the node to its parent
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            
            # Step 5: Push current node onto stack
            stack.append(node)
        
        # The root node is always at the bottom of the stack
        return stack[0] if stack else None
