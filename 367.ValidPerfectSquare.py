class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 1:
            return False

        left, right = 1, num
        while left + 1 < right:
            mid = (left + right) // 2
            midV = mid * mid
            if midV == num:
                return True
            elif midV < num:
                left = mid
            else:
                right = mid
        return left * left == num
