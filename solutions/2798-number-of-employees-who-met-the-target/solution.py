class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        """
        Counts the number of employees who worked at least `target` hours.
        
        Uses a generator expression with sum() to achieve O(n) time and O(1) auxiliary space.
        """
        return sum(1 for h in hours if h >= target)
