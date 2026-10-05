class Solution:
    def numberOfMatches(self, n: int) -> int:
        """
        In a single-elimination tournament:
        - Each match eliminates exactly 1 team.
        - To determine 1 winner from n teams, exactly n - 1 teams must be eliminated.
        - Therefore, exactly n - 1 matches must be played.
        """
        return n - 1
