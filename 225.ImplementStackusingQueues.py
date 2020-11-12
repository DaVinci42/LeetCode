from queue import deque


class MyStack:
    def __init__(self):
        self.queue = deque()
        self.tmp = deque()

    def push(self, x: int) -> None:
        while self.queue:
            self.tmp.append(self.queue.popleft())
        self.queue.append(x)
        while self.tmp:
            self.queue.append(self.tmp.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue
