class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        depth = 0
        
        for char in s:
            if char == '(':
                # If depth > 0, this '(' is NOT the outermost opening parenthesis
                # of the current primitive block.
                if depth > 0:
                    res.append(char)
                depth += 1
            else: # char == ')'
                depth -= 1
                # If depth > 0 after decrement, this ')' is NOT the outermost closing parenthesis
                # of the current primitive block.
                if depth > 0:
                    res.append(char)
                    
        return "".join(res)
