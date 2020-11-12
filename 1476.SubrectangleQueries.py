from typing import List


class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(
        self, row1: int, col1: int, row2: int, col2: int, newValue: int
    ) -> None:
        newSlice = [newValue] * (col2 - col1 + 1)
        for r in range(row1, row2 + 1):
            self.rectangle[r][col1 : col2 + 1] = newSlice

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]
