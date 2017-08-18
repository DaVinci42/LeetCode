"""
257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""


# Definition for a binary tree node.

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        result = []
        self.find_path(root, [], result)
        print(result)
        result = map(lambda p: "->".join(str(i) for i in p), result)
        return result

    def find_path(self, root, pre_path, result):
        pre_path.append(root.val)
        if root.left is None and root.right is None:
            result.append(pre_path)
        if root.left is not None:
            self.find_path(root.left, pre_path[:], result)
        if root.right is not None:
            self.find_path(root.right, pre_path[:], result)
