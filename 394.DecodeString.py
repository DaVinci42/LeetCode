from queue import deque


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c is not "]":
                stack.append(c)
            else:
                cQueue = deque([])
                while stack[-1] != "[":
                    cQueue.appendleft(stack.pop())

                stack.pop()
                numQueue = deque([])
                while stack and stack[-1].isnumeric():
                    numQueue.appendleft(stack.pop())

                stack.append("".join(cQueue) * int("".join(numQueue)))

        return "".join(stack)
