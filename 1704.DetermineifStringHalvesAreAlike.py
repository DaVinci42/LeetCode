class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        length = len(s)
        if length % 2 != 0:
            return False

        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])

        def c(left: int, right: int) -> int:
            return sum(map(lambda i: 1 if i in vowels else 0, s[left:right]))

        return c(0, length // 2) == c(length // 2, length)
