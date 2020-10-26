from typing import Dict
import json

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ""

        indexDict = {}
        self._fillDict(1, root, indexDict)
        return json.dumps(indexDict)

    def _fillDict(self, index: int, node: TreeNode, indexDict: Dict[int, int]):
        indexDict[index] = node.val
        if node.left:
            self._fillDict(index * 2, node.left, indexDict)
        if node.right:
            self._fillDict(index * 2 + 1, node.right, indexDict)

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
        return self._parseDict(1, json.loads(data))

    def _parseDict(self, index: int, indexDict: Dict[int, int]) -> TreeNode:
        if str(index) not in indexDict:
            return None

        n = TreeNode(indexDict[str(index)])
        n.left = self._parseDict(index * 2, indexDict)
        n.right = self._parseDict(index * 2 + 1, indexDict)
        return n
