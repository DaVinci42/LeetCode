class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        negative = False
        if s[0] == '-':
            negative = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        l = []
        for c in s:
            if c.isdigit():
                l.append(c)
            else:
                break
        if not l:
            return 0

        s = int(''.join(l))
        if negative:
            s = -1 * s

        MIN, MAX = -1 << 31, (1 << 31) - 1
        if s < MIN:
            return MIN
        elif s > MAX:
            return MAX
        else:
            return s
