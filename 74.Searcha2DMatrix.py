from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        left, right = 0, len(matrix) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            midV = matrix[mid][0]
            if midV == target:
                return True
            elif midV < target:
                left = mid
            else:
                right = mid

        def searchRow(row: List[int]) -> bool:
            if target < row[0] or target > row[-1]:
                return False
            left, right = 0, len(row) - 1
            while left + 1 < right:
                mid = (left + right) // 2
                midV = row[mid]
                if midV == target:
                    return True
                elif midV < target:
                    left = mid
                else:
                    right = mid
            return row[left] == target or row[right] == target

        return searchRow(matrix[left]) or searchRow(matrix[right])