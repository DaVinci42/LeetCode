from typing import List, Dict


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 1:
            return 0

        maxLeftDict: Dict[int, int] = {}
        maxIndex = 0
        for i in range(0, len(height)):
            if height[i] >= height[maxIndex]:
                maxLeftDict[i] = i
                maxIndex = i
            else:
                maxLeftDict[i] = maxIndex

        maxRightDict: Dict[int, int] = {}
        maxIndex = len(height) - 1
        for i in range(len(height) - 1, -1, -1):
            if height[i] >= height[maxIndex]:
                maxRightDict[i] = i
                maxIndex = i
            else:
                maxRightDict[i] = maxIndex

        area = 0

        for i, h in enumerate(height):
            maxLeft, maxRight = height[maxLeftDict[i]], height[maxRightDict[i]]
            minH = min(maxLeft, maxRight)
            if h >= minH:
                continue
            else:
                area += (minH - h)
                print(i, minH, h)
        return area
