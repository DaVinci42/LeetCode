from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        if not logs:
            return []

        res, funcStack = [0] * n, []
        for l in logs:
            l = l.split(":")
            index, isStart, timeS = int(l[0]), l[1] == "start", int(l[2])

            if isStart:
                if funcStack:
                    curFunc, startT = funcStack[-1]
                    res[curFunc] += timeS - startT

                funcStack.append((index, timeS))
            else:
                curFunc, startT = funcStack.pop()
                res[curFunc] += timeS - startT + 1

                if funcStack:
                    funcStack[-1] = funcStack[-1][0], timeS + 1
        return res
