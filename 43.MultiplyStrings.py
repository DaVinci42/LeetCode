class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        res = [0] * (len(num1) + len(num2))

        for i in range(0, len(num1)):
            for j in range(0, len(num2)):
                r = int(num1[l1 - 1 - i]) * int(num2[l2 - 1 - j])
                index = l1 + l2 - 1 - i - j
                if r < 10:
                    res[index] += r
                else:
                    res[index] += r % 10
                    res[index - 1] += r // 10

        for i in range(len(res) - 1, -1, -1):
            if res[i] >= 10:
                res[i - 1] += res[i] // 10
                res[i] = res[i] % 10

        return "".join(str(n) for n in res).lstrip("0") or "0"
