"""
57. Insert Interval

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""


# Definition for an interval.


class Interval(object):

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if intervals is None or len(intervals) == 0:
            return [newInterval]
        elif newInterval is None:
            return intervals

        intervals.append(newInterval)
        Interval.__lt__ = lambda x, y: x.start < y.start
        intervals.sort()

        result, length = [], len(intervals)
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
