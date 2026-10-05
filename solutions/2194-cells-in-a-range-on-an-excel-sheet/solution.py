class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        # Unpack indices based on the fixed format "<col1><row1>:<col2><row2>"
        c1, r1 = s[0], int(s[1])
        c2, r2 = s[3], int(s[4])
        
        result = []
        
        # Outer loop iterates through columns alphabetically from c1 to c2
        for col_code in range(ord(c1), ord(c2) + 1):
            col_char = chr(col_code)
            # Inner loop iterates through rows numerically from r1 to r2
            for row in range(r1, r2 + 1):
                result.append(f"{col_char}{row}")
                
        return result
