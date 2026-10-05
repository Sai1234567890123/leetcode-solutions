class SubrectangleQueries:

    def __init__(self, rectangle: list[list[int]]):
        """
        Initialize the object with the given matrix and an empty list of updates.
        """
        self.rect = rectangle
        # Stores history of updates as tuples: (row1, col1, row2, col2, newValue)
        self.updates: list[tuple[int, int, int, int, int]] = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        """
        Records the update operation in O(1) time without modifying the underlying grid.
        """
        self.updates.append((row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        """
        Retrieves the value at (row, col) by checking updates in reverse chronological order.
        If no update covers the cell, returns the original matrix value.
        """
        # Iterate backwards from most recent update to oldest
        for r1, c1, r2, c2, val in reversed(self.updates):
            if r1 <= row <= r2 and c1 <= col <= c2:
                return val
        
        # Fall back to initial value if never overwritten
        return self.rect[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
