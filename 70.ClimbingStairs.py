class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 1:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2

        c1, c2 = 1, 2
        for _ in range(n - 2):
            c1, c2 = c2, c1 + c2
        return c2
