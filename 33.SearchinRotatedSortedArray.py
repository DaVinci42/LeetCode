from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while right - left > 1:
            mid = (left + right) // 2
            midV = nums[mid]
            if midV < nums[right]:
                right = mid
            else:
                left = mid

        def biSearch(left: int, right: int, n: int) -> int:
            while right - left > 1:
                mid = (left + right) // 2
                midV = nums[mid]
                if midV == target:
                    return mid
                elif midV > target:
                    right = mid
                else:
                    left = mid
            if nums[left] == n:
                return left
            elif nums[right] == n:
                return right
            else:
                return -1

        head = min(left, right, key=lambda i: nums[i])
        tail = head - 1
        if nums[head] <= target <= nums[-1]:
            left, right = head, len(nums) - 1
            return biSearch(head, len(nums) - 1, target)
        elif nums[0] <= target <= nums[tail]:
            return biSearch(0, tail, target)
        else:
            return -1
