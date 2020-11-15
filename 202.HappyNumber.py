class Solution:
    def isHappy(self, n: int) -> bool:
        resSet = set()

        def check(m: int) -> bool:
            if m == 1:
                return True
            if m == 0 or m in resSet:
                return False
            resSet.add(m)
            res = 0
            while m > 9:
                a = m % 10
                res += a * a
                m = m // 10
            res += m * m
            return check(res)

        return check(n)