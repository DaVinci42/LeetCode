from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target) -> bool:
        if not matrix or not matrix[0]:
            return False

        def searchRow(row: int, l: int, r: int) -> bool:
            row = matrix[row]
            while l + 1 < r:
                mid = (l + r) // 2
                midV = row[mid]
                if midV == target:
                    return True
                elif midV > target:
                    r = mid
                else:
                    l = mid
            return row[l] == target or row[r] == target

        def searchCol(col: int, t: int, b: int) -> bool:
            while t + 1 < b:
                mid = (t + b) // 2
                midV = matrix[mid][col]
                if midV == target:
                    return True
                elif midV > target:
                    b = mid
                else:
                    t = mid
            return matrix[t][col] == target or matrix[b][col] == target

        def search(l: int, t: int, r: int, b: int) -> bool:
            if l > r or t > b:
                return False

            if target < matrix[t][l] or target > matrix[b][r]:
                return False
            if t == b:
                return searchRow(t, l, r)
            elif t + 1 == b:
                return searchRow(t, l, r) or searchRow(b, l, r)
            elif l == r:
                return searchCol(l, t, b)
            elif l + 1 == r:
                return searchCol(l, t, b) or searchCol(r, t, b)

            midR, midC = (t + b) // 2, (l + r) // 2
            midV = matrix[midR][midC]
            if midV == target:
                return True
            elif midV < target:
                return (
                    search(midC, midR, r, b)
                    or search(l, midR + 1, midC, b)
                    or search(midC + 1, t, r, midR)
                )
            else:
                return (
                    search(l, t, midC, midR)
                    or search(l, midR, midC - 1, b)
                    or search(midC, t, r, midR - 1)
                )

        return search(0, 0, len(matrix[0]) - 1, len(matrix) - 1)