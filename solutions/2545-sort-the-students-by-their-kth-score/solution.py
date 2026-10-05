class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        # Sort the rows in-place in descending order based on the k-th column score.
        # Python's Timsort operates on the row references, so the individual
        # row arrays are not copied or re-created, achieving optimal efficiency.
        score.sort(key=lambda row: row[k], reverse=True)
        return score
