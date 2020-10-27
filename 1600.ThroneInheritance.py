from typing import List, Set
from itertools import chain


class Node:
    def __init__(self, name: str, child=None):
        self.name = name
        self.children = []


class ThroneInheritance:
    def __init__(self, kingName: str):
        k = Node(kingName)
        self.kindeName = kingName
        self.nodeMap = {kingName: k}
        self.deadSet = set()

    def birth(self, parentName: str, childName: str) -> None:
        c = Node(childName)
        self.nodeMap[childName] = c
        self.nodeMap[parentName].children.append(c)

    def death(self, name: str) -> None:
        self.deadSet.add(name)

    def getInheritanceOrder(self) -> List[str]:
        def rec(name: str) -> List[str]:
            n = self.nodeMap[name]
            return list(
                chain(
                    [] if name in self.deadSet else [name],
                    *[rec(c.name) for c in n.children]
                )
            )

        return rec(self.kindeName)
