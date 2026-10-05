class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        
        # In binary representation:
        # - Subtracting 1 flips a set bit (1 -> 0).
        # - Dividing by 2 right-shifts the bits by 1.
        #
        # Each set bit ('1') requires:
        #   1 step to subtract (except the most significant bit) + 1 step to shift right.
        # Each unset bit ('0') requires:
        #   1 step to shift right.
        #
        # Total steps = (total bits - 1) + (count of set bits)
        # where (total bits - 1) is the number of right shifts,
        # and (count of set bits) is the number of subtractions.
        return (num.bit_length() - 1) + num.bit_count()
