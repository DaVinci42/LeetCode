from typing import List
from queue import PriorityQueue


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = PriorityQueue()
        for n in nums:
            q.put(-1 * n)

        for _ in range(k - 1):
            q.get()
        return -1 * q.get()