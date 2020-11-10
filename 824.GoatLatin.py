class Solution:
    def toGoatLatin(self, S: str) -> str:
        if not S:
            return ""

        res = S.split(" ")
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        for i, word in enumerate(res):
            if word[0] in vowels:
                word += "ma"
            else:
                word = word[1:] + word[0] + "ma"
            res[i] = word + "a" * (i + 1)
        return " ".join(res)
