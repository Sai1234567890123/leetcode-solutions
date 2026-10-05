class Solution:
    def balancedStringSplit(self, s: str) -> int:
        """
        Greedily split the string at every point where the count of 'R' and 'L' becomes equal.
        """
        balance = 0
        balanced_count = 0
        
        for char in s:
            # Increment for 'R' and decrement for 'L' (or vice-versa)
            if char == 'R':
                balance += 1
            else:
                balance -= 1
            
            # Whenever balance returns to zero, we've found a minimal balanced substring
            if balance == 0:
                balanced_count += 1
                
        return balanced_count
