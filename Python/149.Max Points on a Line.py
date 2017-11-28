"""
149. Max Points on a Line

Given n points on a 2D plane,
find the maximum number of points that lie on the same straight line.
"""

# Definition for a point.


class Point:

    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if points is None or len(points) == 0:
            return 0
        if len(points) == 1:
            return 1

        l_set, handled_point = set(), set()
        for p in points:
            x1, y1 = p.x, p.y
            if (x1, y1) in handled_point:
                continue

            for hp in handled_point:
                x2, y2 = hp.x, hp.y
                a = y2 - y1
                b = x1 - x2
                c = x2 * y1 - x1 * y2
                if a != 0 or b != 0 or c != 0:
                    l_set.add((a, b, c))

            handled_point.add(p)

        if len(l_set) == 0:
            return len(points)

        l_dict = dict()
        for line in l_set:
            a, b, c = line
            for p in points:
                x, y = p.x, p.y
                if a * x + b * y + c == 0:
                    count = 0 if line not in l_dict else l_dict[line]
                    l_dict[line] = count + 1

        return max(l_dict.values())
