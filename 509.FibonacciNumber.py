class Solution:
    def fib(self, N: int) -> int:
        if N <= 0:
            return 0
        elif N == 1:
            return 1

        n0, n1 = 0, 1
        for _ in range(N - 1):
            n0, n1 = n1, n0 + n1
        return n1
