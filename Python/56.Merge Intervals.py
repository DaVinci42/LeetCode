"""
56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""

# Definition for an interval.


class Interval(object):

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        if intervals is None or len(intervals) == 0:
            return result

        Interval.__lt__ = lambda x, y: x.start < y.start
        intervals.sort()

        length = len(intervals)
        for i in range(0, length):
            now = intervals[i]
            if len(result) == 0:
                result.append(now)
            else:
                pre = result[-1]
                if pre.end >= now.start:
                    pre.start = min(pre.start, now.start)
                    pre.end = max(pre.end, now.end)
                else:
                    result.append(now)
        return result
