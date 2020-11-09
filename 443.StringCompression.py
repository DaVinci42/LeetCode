from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) <= 1:
            return len(chars)

        index, left = 0, 0
        for right in range(0, len(chars)):
            if chars[right] == chars[left]:
                continue
            else:
                count = right - left
                if count == 1:
                    chars[index] = chars[left]
                    index += 1
                else:
                    chars[index] = chars[left]
                    index += 1
                    s = str(count)
                    for i in range(0, len(s)):
                        chars[index] = s[i]
                        index += 1
                left = right

        if left == len(chars) - 1:
            chars[index] = chars[left]
            index += 1
        else:
            chars[index] = chars[left]
            index += 1
            count = len(chars) - left
            s = str(count)
            for i in range(0, len(s)):
                chars[index] = s[i]
                index += 1
        return index
