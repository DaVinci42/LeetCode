from typing import List
from collections import deque


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or sum(candidates) < target:
            return []
        self.candidates = candidates
        self.target = target
        self.candidates.sort()
        self.result = set()
        self.find(0, deque(), 0)
        return list(self.result)

    def find(self, index: int, q: deque, preSum: int):
        if index >= len(self.candidates):
            return

        if preSum + self.candidates[index] > self.target:
            return

        v = self.candidates[index]
        q0 = deque(q)
        q0.append(v)
        if preSum + v == self.target:
            self.result.add(tuple(q0))

        self.find(index + 1, q0, preSum + v)

        q1 = deque(q)
        self.find(index + 1, q1, preSum)
