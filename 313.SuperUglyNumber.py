from typing import List
import heapq


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1 or not primes:
            return 1

        heap = [1]
        for _ in range(n - 1):
            minV = heapq.heappop(heap)
            while heap and heap[0] == minV:
                heapq.heappop(heap)

            for p in primes:
                heapq.heappush(heap, p * minV)
        return heap[0]
