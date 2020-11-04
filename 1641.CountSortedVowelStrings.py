class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n < 1:
            return 0
        elif n == 1:
            return 5

        n1, n2, n3, n4, n5 = 1, 1, 1, 1, 1
        for _ in range(n - 1):
            n1, n2, n3, n4, n5 = (
                n1,
                n1 + n2,
                n1 + n2 + n3,
                n1 + n2 + n3 + n4,
                n1 + n2 + n3 + n4 + n5,
            )

        return n1 + n2 + n3 + n4 + n5
