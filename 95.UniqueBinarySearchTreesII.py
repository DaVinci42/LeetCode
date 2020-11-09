from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n <= 0:
            return []

        def generate(nums: List[int]) -> List[TreeNode]:
            if not nums:
                return [None]
            elif len(nums) == 1:
                return [TreeNode(nums[0])]

            res = []
            for i, num in enumerate(nums):
                leftNodes = generate(nums[:i])
                rightNodes = generate(nums[i + 1 :])

                for a in leftNodes:
                    for b in rightNodes:
                        node = TreeNode(num)
                        node.left = a
                        node.right = b
                        res.append(node)
            return res

        return generate(list(range(1, n + 1)))

