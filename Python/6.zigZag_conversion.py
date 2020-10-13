import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or numRows <= 1:
            return s

        unit = int(math.ceil(len(s) / (2 * numRows - 2)))
        groups = [s[i * 2 * (numRows - 1): min(len(s), (i + 1) * 2 * (numRows - 1))]
                  for i in range(0, unit)]

        output = []
        for i in range(0, numRows):
            for g in groups:
                if i == 0:
                    output.append(g[0])
                elif i == numRows - 1 and numRows - 1 <= len(g) - 1:
                    output.append(g[numRows - 1])
                else:
                    left, right = i, 2 * numRows - 2 - i
                    if left < len(g):
                        output.append(g[left])
                    if right < len(g):
                        output.append(g[right])

        return "".join(output)
