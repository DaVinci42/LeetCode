class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x1 = x
        n = 0
        while x1 > 0:
            n *= 10
            n += x1 % 10
            x1 //= 10
        return n == x
