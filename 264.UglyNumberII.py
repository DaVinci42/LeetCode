from queue import deque


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1

        d2, d3, d5 = deque([1]), deque([1]), deque([1])
        res = 1
        for _ in range(1, n):
            minV = min(d2[0] * 2, d3[0] * 3, d5[0] * 5)
            if d2[0] * 2 == minV:
                d2.popleft()
            if d3[0] * 3 == minV:
                d3.popleft()
            if d5[0] * 5 == minV:
                d5.popleft()

            d2.append(minV)
            d3.append(minV)
            d5.append(minV)
            res = minV
        return res
