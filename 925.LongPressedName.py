class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l = list(typed)
        for i in range(len(name) - 1, -1, -1):
            c = name[i]
            if not l or l[-1] != c:
                return False
            if i > 0 and name[i - 1] == c:
                del l[-1]
            else:
                while l and l[-1] == c:
                    del l[-1]

        return not l