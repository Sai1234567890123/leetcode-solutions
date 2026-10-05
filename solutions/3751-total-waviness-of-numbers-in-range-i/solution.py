class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        """
        Calculates the total waviness of all numbers in the inclusive range [num1, num2].
        A peak occurs at index i if s[i-1] < s[i] > s[i+1].
        A valley occurs at index i if s[i-1] > s[i] < s[i+1].
        """
        total_waviness = 0
        
        for num in range(num1, num2 + 1):
            s = str(num)
            n = len(s)
            
            # Numbers with fewer than 3 digits cannot have peaks or valleys
            if n < 3:
                continue
                
            # Count peaks and valleys for the current number
            for i in range(1, n - 1):
                prev_d, curr_d, next_d = s[i - 1], s[i], s[i + 1]
                if (curr_d > prev_d and curr_d > next_d) or (curr_d < prev_d and curr_d < next_d):
                    total_waviness += 1
                    
        return total_waviness
