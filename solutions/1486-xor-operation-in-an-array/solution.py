class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        def xor_prefix(k: int) -> int:
            """Helper function to compute XOR from 0 to k in O(1)."""
            rem = k % 4
            if rem == 0:
                return k
            elif rem == 1:
                return 1
            elif rem == 2:
                return k + 1
            else:
                return 0

        # We can express start + 2 * i as: 2 * (start // 2 + i) + (start % 2)
        # 1. Least Significant Bit (LSB):
        # Each element has the same LSB, which is (start & 1).
        # When XORed n times, it contributes 1 if both (start & 1) and (n & 1) are 1.
        lsb = (n & start & 1)

        # 2. Higher bits:
        # Shifting right by 1, the sequence becomes consecutive integers:
        # s, s + 1, s + 2, ..., s + n - 1, where s = start // 2.
        s = start >> 1
        higher_bits_xor = xor_prefix(s + n - 1) ^ xor_prefix(s - 1)

        # Combine the higher bits shifted back left by 1 and the LSB
        return (higher_bits_xor << 1) | lsb
