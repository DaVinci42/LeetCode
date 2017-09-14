"""
347. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 <= k <= number of unique elements.
Your algorithm's time complexity must be better than O(n log n),
where n is the array's size.
"""


class Solution(object):

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return list()
        if k <= 0 or k > len(nums):
            return list()

        count_dict = dict()
        for n in nums:
            count = 0 if n not in count_dict else count_dict[n]
            count_dict[n] = count + 1

        count_list = list(count_dict.values())
        count_list.sort()
        count_list = count_list[::-1][0:k]
        target_set = set(count_list)

        result = list()
        for n in count_dict:
            count = count_dict[n]
            if count in target_set:
                result.append(n)
        if len(result) > k:
            result = result[0:k]
        return result
