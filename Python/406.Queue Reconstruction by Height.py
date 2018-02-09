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
            h = p[0]
            group = set() if h not in height_dict else height_dict[h]
            group.add((h, p[1]))
            height_dict[h] = group

        heights = list(height_dict.keys())
        heights.sort()

        people_count = len(people)
        index_list = [i for i in range(0, people_count)]
        result_queue = [0] * people_count

        for i in heights:
            group = list(height_dict[i])
            group.sort()
            reversed_p = group[::-1]
            for p in reversed_p:
                k = p[1]
                target = index_list[k]
                result_queue[target] = p
                del index_list[k]

        return list(map(lambda p: list([p[0], p[1]]), result_queue))
