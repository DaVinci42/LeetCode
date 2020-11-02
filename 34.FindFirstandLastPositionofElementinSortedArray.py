from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def findFirst(n: int) -> int:
            if nums[0] == n:
                return 0
            elif nums[0] > n:
                return -1

            left, right = 0, len(nums) - 1
            while right - left > 1:
                mid = (left + right) // 2
                midV = nums[mid]
                if midV >= n:
                    right = mid
                else:
                    left = mid
            if nums[left] == n:
                return left
            elif nums[right] == n:
                return right
            else:
                return -1

        def findLast(n: int) -> int:
            if nums[-1] == n:
                return len(nums) - 1
            elif nums[-1] < n:
                return -1

            left, right = 0, len(nums) - 1
            while right - left > 1:
                mid = (left + right) // 2
                midV = nums[mid]
                if midV <= n:
                    left = mid
                else:
                    right = mid
            if nums[right] == n:
                return right
            elif nums[left] == n:
                return left
            else:
                return -1

        return [findFirst(target), findLast(target)]
