class MyQueue:
    def __init__(self):
        self.stack = []
        self.tmp = []

    def push(self, x: int) -> None:
        while self.stack:
            self.tmp.append(self.stack.pop())
        self.stack.append(x)
        while self.tmp:
            self.stack.append(self.tmp.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not self.stack
