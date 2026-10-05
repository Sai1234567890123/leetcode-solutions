class Solution:
    def countAsterisks(self, s: str) -> int:
        asterisk_count = 0
        inside_pair = False

        for char in s:
            if char == '|':
                # Toggle state: entering or exiting a pair of '|'
                inside_pair = not inside_pair
            elif char == '*' and not inside_pair:
                # Count asterisks only when outside any '|' pair
                asterisk_count += 1

        return asterisk_count
