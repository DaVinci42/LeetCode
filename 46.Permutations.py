from typing import List, Set
import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(lambda t: list(t), itertools.permutations(nums)))
