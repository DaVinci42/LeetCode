from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        length = len(nums)
        if length < 4:
            return []

        result = []
        nums.sort()
        for a in range(0, length - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            for b in range(a + 1, length - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                expect = target - nums[a] - nums[b]
                c, d = b + 1, length - 1
                while c < d:
                    if c > b + 1 and nums[c] == nums[c - 1]:
                        c += 1
                        continue
                    if d < length - 1 and nums[d] == nums[d + 1]:
                        d -= 1
                        continue

                    s = nums[c] + nums[d]
                    if s == expect:
                        result.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                    elif s > expect:
                        d -= 1
                    else:
                        c += 1

        return result
