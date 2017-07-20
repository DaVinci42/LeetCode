"""
93. Restore IP Addresses

Given a string containing only digits,
restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""


class Solution(object):

    result = []

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if s is None or len(s) == 0:
            return []
        if len(s) > 12:
            return []

        self.result = []
        self.address_parse(s, 0, 4, [])
        return self.result

    def address_parse(self, s, index, left, pre_ad):
        length = len(s)

        if left == 0 and index == length:
            address = ""
            for n in pre_ad:
                if ((len(n) == 3 and int(n) < 100) or
                        (len(n) == 2 and int(n) < 10)):
                    return

                address += (n + ".")
            self.result.append(address[0:-1])

        if length - index < left:
            return
        if index <= length - 1:
            n = int(s[index])
            ad = pre_ad[:]
            ad.append(str(n))
            self.address_parse(s, index + 1, left - 1, ad)
        if index <= length - 2:
            n = int(s[index]) * 10 + int(s[index + 1])
            ad = pre_ad[:]
            ad.append(s[index:index + 2])
            self.address_parse(s, index + 2, left - 1, ad)
        if index <= length - 3:
            n = int(s[index]) * 100 + int(s[index + 1]) * \
                10 + int(s[index + 2])
            if n <= 255:
                ad = pre_ad[:]
                ad.append(s[index:index + 3])
                self.address_parse(s, index + 3, left - 1, ad)
