from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4:
            return []

        def isValid(left: int, right: int) -> bool:
            if right - left == 1:
                return True
            elif right - left == 2 and s[left] != "0":
                return True
            elif right - left == 3 and s[left] != "0" and int(s[left:right]) <= 255:
                return True
            else:
                return False

        def search(index: int, parts: int) -> List[str]:
            res, leftNum = [], len(s) - index
            if not parts <= leftNum <= 3 * parts:
                return res

            if parts == 1:
                return [s[index:]] if isValid(index, len(s)) else []
            else:
                if leftNum >= 3 and isValid(index, index + 3):
                    for i in search(index + 3, parts - 1):
                        res.append(f"{s[index:index+3]}.{i}")
                if leftNum >= 2 and isValid(index, index + 2):
                    for i in search(index + 2, parts - 1):
                        res.append(f"{s[index:index + 2]}.{i}")
                if leftNum >= 1 and isValid(index, index + 1):
                    for i in search(index + 1, parts - 1):
                        res.append(f"{s[index]}.{i}")
            return res

        return search(0, 4)
