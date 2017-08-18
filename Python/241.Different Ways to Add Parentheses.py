"""
241. Different Ways to Add Parentheses

Given a string of numbers and operators,
return all possible results from computing all the different possible ways to group numbers and operators.
The valid operators are +, - and *.

Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
"""


class Solution(object):

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input is None or len(input) == 0:
            return []

        lis, tmp = list(), ""
        for c in input:
            if c == "+" or c == "-" or c == "*":
                lis.append(tmp)
                lis.append(c)
                tmp = ""
            else:
                tmp += c
        lis.append(tmp)

        way_set = set()
        self.find_ways(lis, way_set)
        return map(lambda x: eval(x), way_set)

    def find_ways(self, lis, way_set):
        if len(lis) == 1:
            way_set.add(lis[0])
            return

        for i, c in enumerate(lis):
            if c == "+" or c == "-" or c == "*":
                left, right = lis[i - 1], lis[i + 1]
                copy = lis[:]

                del copy[i + 1]
                del copy[i]
                del copy[i - 1]
                copy.insert(i - 1, "(" + left + c + right + ")")

                self.find_ways(copy, way_set)
