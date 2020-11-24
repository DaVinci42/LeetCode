class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not num1:
            return num2
        if not num2:
            return num1

        i1, i2, carry, res = len(num1) - 1, len(num2) - 1, False, []
        while i1 >= 0 or i2 >= 0 or carry:
            d = 1 if carry else 0
            if i1 >= 0:
                d += int(num1[i1])
                i1 -= 1
            if i2 >= 0:
                d += int(num2[i2])
                i2 -= 1

            carry = d >= 10
            res.append(str(d % 10))

        return "".join(res[::-1])