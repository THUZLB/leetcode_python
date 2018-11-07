# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        r = ''
        roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        m = num // 1000
        r += 'M' * m
        num -= 1000 * m

        c = num // 100
        if c == 9:
            r += 'CM'
        elif c > 4:
            r += 'D'
            num -= 500
            c = num // 100
            r += 'C' * c
        elif c == 4:
            r += 'CD'
        else:
            r += 'C' * c
        num -= 100 * c

        x = num // 10
        if x == 9:
            r += 'XC'
        elif x > 4:
            r += 'L'
            num -= 50
            x = num // 10
            r += 'X' * x
        elif x == 4:
            r += 'XL'
        else:
            r += 'X' * x
        num -= 10 * x

        if num == 9:
            r += 'IX'
        elif num > 4:
            r += 'V'
            num -= 5
            r += 'I' * num
        elif num ==4:
            r += 'IV'
        else:
            r += 'I' * num

        return r


# best solution in leetcode
# class Solution:
#     def intToRoman(self, num):
#         """
#         :type num: int
#         :rtype: str
#         """
#         M = ["", "M", "MM", "MMM"];
#         C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
#         X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
#         I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
#
#         return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10];

# test
num = 1994
solution = Solution()
print(solution.intToRoman(num))
