from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        if n < 1:
            return []

        def convert(i: int) -> str:
            if i % 3 == 0 and i % 5 == 0:
                return "FizzBuzz"
            elif i % 3 == 0:
                return "Fizz"
            elif i % 5 == 0:
                return "Buzz"
            else:
                return str(i)

        return list(map(convert, range(1, n + 1)))
