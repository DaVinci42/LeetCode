"""
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s is None or len(s) == 0 or len(s) == 1 or numRows == 1:
            return s
        all_row = []
        for i in range(0, numRows):
            row = []
            all_row.append(row)

        for index, value in enumerate(s):
            row_num = self.get_row_of_char(numRows, index)
            all_row[row_num].append(value)

        result = ""
        for list in all_row:
            for char in list:
                result += char
        return result

    def get_row_of_char(self, numRows, index):
        mod = 2 * numRows - 2
        idx = index % mod
        if idx < numRows:
            return idx
        else:
            return 2 * (numRows - 1) - idx


s = Solution()
print(s.convert("PAYPALISHIRING", 3))
