'''
436. Find Right Interval

Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:
You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
Example 1:
Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.
Example 2:
Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.
Example 3:
Input: [ [1,4], [2,3], [3,4] ]

Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.
'''

# Definition for an interval.


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        if intervals is None or len(intervals) == 0:
            return list()

        start_list = list()
        start_dict = dict()
        for i, v in enumerate(intervals):
            start_list.append(v.start)
            start_dict[v.start] = i
        start_list.sort()

        result_list = map(
            lambda x: self.findNearestStart(x.end, start_list), intervals)
        return list(map(lambda x: -1 if x is None else start_dict[x], result_list))

    def findNearestStart(self, target, start_list):
        if target <= start_list[0]:
            return start_list[0]
        if target > start_list[-1]:
            return None

        left, right = 0, len(start_list) - 1
        while right - left > 1:
            mid = (left + right) // 2
            mid_v = start_list[mid]
            if mid_v == target:
                return mid_v
            if mid_v > target:
                right = mid
            else:
                left = mid
        return start_list[right]
