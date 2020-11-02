class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        map = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for c in s:
            if c not in map:
                if not stack or map[stack.pop()] != c:
                    return False
            else:
                stack.append(c)
        return not stack
