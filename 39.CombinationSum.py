from typing import List
from collections import deque


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        self.candidates = candidates
        self.candidates.sort()
        self.target = target
        self.result = []
        self.find(0, 0, deque())
        return self.result

    def find(self, index: int, preSum: int, q: deque):
        if index >= len(self.candidates):
            return

        v = self.candidates[index]
        if preSum + v > self.target:
            return

        allowedCount = (self.target - preSum) // v
        for i in range(0, allowedCount + 1):
            dq = deque(q)
            dq.extend([v] * i)
            s = preSum + v * i
            if s == self.target:
                self.result.append(list(dq))

            self.find(index + 1, s, dq)
