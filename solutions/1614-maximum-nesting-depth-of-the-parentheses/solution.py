class Solution:
    def maxDepth(self, s: str) -> int:
        """
        Calculates the maximum nesting depth of a valid parentheses string.
        
        Time Complexity: O(n) where n is the length of the string s.
        Space Complexity: O(1) auxiliary space.
        """
        max_depth = 0
        current_depth = 0
        
        for char in s:
            if char == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ')':
                current_depth -= 1
                
        return max_depth
