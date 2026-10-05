class Solution:
    def maximum69Number (self, num: int) -> int:
        temp = num
        position = 0
        leftmost_six_pos = -1

        # Traverse digits from right to left (least significant to most significant)
        while temp > 0:
            digit = temp % 10
            if digit == 6:
                # Update the position of the 6 found; since we move right-to-left,
                # the last 6 we encounter will be the most significant (leftmost).
                leftmost_six_pos = position
            temp //= 10
            position += 1

        # If a '6' was found, changing it to '9' adds 3 * (10 ** position)
        if leftmost_six_pos != -1:
            return num + 3 * (10 ** leftmost_six_pos)
        
        return num
