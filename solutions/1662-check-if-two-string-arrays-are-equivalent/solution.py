class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        # Pointers for word1: word index and character index
        w1_idx, c1_idx = 0, 0
        # Pointers for word2: word index and character index
        w2_idx, c2_idx = 0, 0
        
        len1, len2 = len(word1), len(word2)
        
        # Traverse both arrays simultaneously without concatenating
        while w1_idx < len1 and w2_idx < len2:
            # If characters at current positions do not match, return False
            if word1[w1_idx][c1_idx] != word2[w2_idx][c2_idx]:
                return False
            
            # Advance character pointer in word1
            c1_idx += 1
            # If end of current string in word1 is reached, move to the next string
            if c1_idx == len(word1[w1_idx]):
                w1_idx += 1
                c1_idx = 0
                
            # Advance character pointer in word2
            c2_idx += 1
            # If end of current string in word2 is reached, move to the next string
            if c2_idx == len(word2[w2_idx]):
                w2_idx += 1
                c2_idx = 0
                
        # Both arrays must be completely consumed at the same time
        return w1_idx == len1 and w2_idx == len2
