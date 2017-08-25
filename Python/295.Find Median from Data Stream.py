"""
295. Find Median from Data Stream

Median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
"""


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.nums) == 0:
            self.nums.append(num)
        elif num <= self.nums[0]:
            self.nums.insert(0, num)
        elif num >= self.nums[-1]:
            self.nums.append(num)
        else:
            left, right = 0, len(self.nums) - 1
            while right - left > 1:
                mid = (left + right) // 2
                mid_v = self.nums[mid]
                if mid_v == num:
                    self.nums.insert(mid, num)
                    return
                elif mid_v < num:
                    left = mid
                else:
                    right = mid
            self.nums.insert(right, num)

    def findMedian(self):
        """
        :rtype: float
        """
        length = len(self.nums)
        if length == 0:
            return 0
        if length % 2 == 0:
            return (self.nums[length // 2 - 1] + self.nums[length // 2]) / 2.0
        else:
            return self.nums[length // 2]
