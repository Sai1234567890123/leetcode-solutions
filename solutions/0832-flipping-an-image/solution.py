class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        """
        Flips the binary matrix horizontally and inverts it in-place.
        """
        n = len(image)
        mid = (n + 1) // 2
        
        for row in image:
            for j in range(mid):
                k = n - 1 - j
                # Key insight:
                # If row[j] == row[k], flipping swaps identical values,
                # then inverting flips both values (0 -> 1 or 1 -> 0).
                # If row[j] != row[k], flipping swaps 0 and 1 to 1 and 0,
                # and inverting swaps them back to 0 and 1, leaving them unchanged!
                if row[j] == row[k]:
                    row[j] = row[k] = row[j] ^ 1
                    
        return image
