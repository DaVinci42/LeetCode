class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n <= 2:
            return 1

        n0, n1, n2 = 0, 1, 1
        for _ in range(n - 2):
            n0, n1, n2 = n1, n2, n0 + n1 + n2
        return n2
