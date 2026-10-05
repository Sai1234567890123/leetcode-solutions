class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        depth = 0
        
        for ch in seq:
            if ch == '(':
                # Assign '(' based on the current nesting level before incrementing
                ans.append(depth % 2)
                depth += 1
            else:
                # Decrement depth first so ')' matches the depth of its corresponding '('
                depth -= 1
                ans.append(depth % 2)
                
        return ans
