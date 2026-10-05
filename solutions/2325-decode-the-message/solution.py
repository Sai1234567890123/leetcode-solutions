class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # Map space to space by default
        mapping = {' ': ' '}
        curr_code = ord('a')
        
        # Build the substitution cipher table from the first appearance of each letter
        for ch in key:
            if ch not in mapping:
                mapping[ch] = chr(curr_code)
                curr_code += 1
                # Early exit if all 26 letters have been mapped
                if curr_code > ord('z'):
                    break
        
        # Decode the message using the substitution mapping
        return "".join(mapping[ch] for ch in message)
