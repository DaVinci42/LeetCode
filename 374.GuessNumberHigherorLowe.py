# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, (1 << 31) - 1
        if guess(left) == 0:
            return left
        elif guess(right) == 0:
            return right

        while right - left > 1:
            mid = (left + right) // 2
            v = guess(mid)
            if v == 0:
                return mid
            elif v > 0:
                left = mid
            else:
                right = mid
        if guess(left):
            return left
        else:
            return right
