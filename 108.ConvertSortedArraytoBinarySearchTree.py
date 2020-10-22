from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.build(nums, 0, len(nums) - 1)

    def build(self, nums: List[int], left: int, right: int) -> TreeNode:
        if left > right or left < 0 or right > len(nums):
            return None
        elif left == right:
            return TreeNode(nums[left])

        mid = (left + right) // 2
        return TreeNode(
            nums[mid], self.build(nums, left, mid - 1), self.build(nums, mid + 1, right)
        )
