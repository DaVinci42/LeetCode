"""
17. Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits is None or len(digits) == 0:
            return []

        num_letters = {}
        num_letters['2'] = ['a', 'b', 'c']
        num_letters['3'] = ['d', 'e', 'f']
        num_letters['4'] = ['g', 'h', 'i']
        num_letters['5'] = ['j', 'k', 'l']
        num_letters['6'] = ['m', 'n', 'o']
        num_letters['7'] = ['p', 'q', 'r', 's']
        num_letters['8'] = ['t', 'u', 'v']
        num_letters['9'] = ['w', 'x', 'y', 'z']

        result = []
        self.print_letters(digits, 0, [], num_letters, result)
        return result

    def print_letters(self, digits, index, pre_list, map, output):
        num = digits[index]
        for letter in map[num]:
            list = pre_list[:]
            list.append(letter)
            if index < len(digits) - 1:
                self.print_letters(digits, index + 1, list, map, output)
            else:
                string = ''.join(list)
                output.append(string)
