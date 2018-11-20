"""
207. Course Schedule

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""


class Solution:

    def canFinish(self, n, pairs):
        """
        :type n: int
        :type pairs: List[List[int]]
        :rtype: bool
        """
        if not n or not pairs:
            return True

        pre_dict, post_dict = dict(), dict()
        for p in pairs:
            pre, post = p[1], p[0]
            pre_set = set() if post not in pre_dict else pre_dict[post]
            post_set = set() if pre not in post_dict else post_dict[pre]
            pre_set.add(pre)
            post_set.add(post)
            pre_dict[post] = pre_set
            post_dict[pre] = post_set

        tasks = set(range(0, n)).difference(pre_dict.keys())

        while tasks:
            learned = tasks.pop()
            if learned not in post_dict:
                continue

            post_set = post_dict[learned]
            if not len(post_set):
                del post_dict[learned]
                continue
            for post in post_set:
                if post not in pre_dict:
                    continue
                pre_set = pre_dict[post]
                if learned in pre_set:
                    pre_set.remove(learned)
                if not len(pre_set):
                    tasks.add(post)
                    del pre_dict[post]
                    continue

        return len(pre_dict) == 0
