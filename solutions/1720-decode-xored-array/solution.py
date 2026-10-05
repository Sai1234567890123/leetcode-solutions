class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        """
        Decodes the XOR-encoded array using the property:
        If a ^ b = c, then b = a ^ c.
        Given arr[i] and encoded[i] = arr[i] ^ arr[i + 1],
        we have arr[i + 1] = arr[i] ^ encoded[i].
        """
        n = len(encoded) + 1
        arr = [0] * n
        arr[0] = first
        
        # Sequentially derive each next element from the current element and encoded value
        for i in range(len(encoded)):
            arr[i + 1] = arr[i] ^ encoded[i]
            
        return arr
