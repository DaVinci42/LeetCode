"""
297. Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""

# Definition for a binary tree node.


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return str()
        dic = dict()
        self.tree_to_dict(root, 1, dic)
        result = str()

        for index in dic:
            if len(result) > 0:
                result += ","
            result += (str(index) + ":" + str(dic[index]))
        return result

    def tree_to_dict(self, node, index, dic):
        dic[index] = node.val
        if node.left is not None:
            self.tree_to_dict(node.left, 2 * index, dic)
        if node.right is not None:
            self.tree_to_dict(node.right, 2 * index + 1, dic)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data is None or len(data) == 0:
            return None
        node_list, node_dict = data.split(","), dict()
        for node in node_list:
            i, v = node.split(":")
            node_dict[int(i)] = int(v)
        return self.dict_to_tree(1, node_dict)

    def dict_to_tree(self, index, dic):
        if index not in dic:
            return None
        n = TreeNode(dic[index])
        n.left = self.dict_to_tree(2 * index, dic)
        n.right = self.dict_to_tree(2 * index + 1, dic)
        return n
