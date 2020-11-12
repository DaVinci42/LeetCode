from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        curSum = 0
        sumDict, res = {0: 1}, 0
        for n in nums:
            curSum += n
            res += sumDict.get(curSum - k, 0)
            sumDict[curSum] = sumDict.get(curSum, 0) + 1
        return res
