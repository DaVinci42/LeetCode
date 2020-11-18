class Solution:
    def convertToTitle(self, n: int) -> str:
        if n == 0:
            return "Z"
        elif 1 <= n <= 26:
            return chr(ord("A") + n - 1)
        else:
            if n % 26 == 0:
                return self.convertToTitle(n // 26 - 1) + "Z"
            else:
                return self.convertToTitle(n // 26) + self.convertToTitle(n % 26)
