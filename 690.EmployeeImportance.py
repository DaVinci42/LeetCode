from typing import List
from queue import deque

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List[Employee], id: int) -> int:
        if not employees:
            return 0
        cache = {e.id: e for e in employees}
        d, res = deque([cache[id]]), 0
        while d:
            for _ in range(len(d)):
                e = d.popleft()
                res += e.importance
                for sub in e.subordinates:
                    d.append(cache[sub])
        return res