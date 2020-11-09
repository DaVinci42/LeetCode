from typing import List
import itertools


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return [list(t) for t in set(itertools.permutations(nums))]
