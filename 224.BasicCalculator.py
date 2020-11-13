from queue import deque
from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        def calWithoutParentheses(input: List) -> int:
            if not input:
                return 0
            stack = []
            for i in input:
                if i == "+" or i == "-":
                    stack.append(i)
                else:
                    if not stack:
                        stack.append(i)
                    elif stack[-1] == "+":
                        stack.pop()
                        stack.append(stack.pop() + i)
                    else:
                        stack.pop()
                        stack.append(stack.pop() - i)
            return stack[0]

        res, i = [], 0
        while i < len(s):
            c = s[i]
            if c == " ":
                i += 1
            elif c == "(" or c == "+" or c == "-":
                res.append(c)
                i += 1
            elif c == ")":
                d = deque()
                while res[-1] != "(":
                    d.appendleft(res.pop())
                res.pop()
                res.append(calWithoutParentheses(d))
                i += 1
            else:
                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1
                res.append(int(s[i:j]))
                i = j

        return calWithoutParentheses(res)
