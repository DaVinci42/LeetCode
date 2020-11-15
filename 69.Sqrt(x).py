class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 0:
            return 0

        left, right = 1, x
        while left + 1 < right:
            mid = (left + right) // 2
            midV = mid * mid
            if midV == x:
                return mid
            elif midV < x:
                left = mid
            else:
                right = mid
        return left
