class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        temp = num
        
        # Extract each digit mathematically to avoid string conversion overhead
        while temp > 0:
            digit = temp % 10
            if num % digit == 0:
                count += 1
            temp //= 10
            
        return count
