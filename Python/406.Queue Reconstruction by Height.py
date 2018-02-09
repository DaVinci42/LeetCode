"""
406. Queue Reconstruction by Height

Suppose you have a random list of people standing in a queue.
Each person is described by a pair of integers (h, k),
where h is the height of the person,
and k is the number of people in front of this person who have a height greater than or equal to h.
Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""


class Solution:

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if people is None or len(people) == 0:
            return list()

        height_dict = dict()
        for p in people:
            h, k = p
            greater_set = set() if h not in height_dict else height_dict[h]
            greater_set.add(k)
            height_dict[h] = greater_set

        heights = list(height_dict.keys())
        heights.sort()

        people_count = len(people)
        index_list = [i for i in range(0, people_count)]
        result_queue = [0] * people_count

        for h in heights:
            greater_list = list(height_dict[h])
            greater_list.sort()
            reversed_list = greater_list[::-1]
            for k in reversed_list:
                target = index_list[k]
                result_queue[target] = list([h, k])
                del index_list[k]
        return result_queue
