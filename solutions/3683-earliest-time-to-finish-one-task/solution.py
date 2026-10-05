class Solution:
    def earliestTime(self, tasks: list[list[int]]) -> int:
        """
        Calculates the earliest completion time among all given tasks.
        
        Each task is represented by [start_time, duration].
        The completion time for a task is start_time + duration.
        """
        # Find the minimum completion time across all tasks
        return min(start + duration for start, duration in tasks)
