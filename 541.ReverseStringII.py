class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if k <= 1:
            return s

        n = len(s)
        res, reverse = [], True
        for i in range(0, n // k):
            r = s[i * k : i * k + k]
            res += r if not reverse else r[::-1]
            reverse = not reverse
        r = s[n - n % k : n]
        res += r if not reverse else r[::-1]
        return "".join(res)
