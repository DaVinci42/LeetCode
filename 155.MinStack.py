class MinStack:
    def __init__(self):
        self.nums = []
        self.mins = []

    def push(self, x: int) -> None:
        self.nums.append(x)
        self.mins.append(x if not self.mins else min(x, self.mins[-1]))

    def pop(self) -> None:
        self.nums.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.mins[-1]
