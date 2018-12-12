# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        negative = False if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else True
        quotient = 0

        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            tmp1 = divisor
            tmp2 = 1
            while dividend >= (divisor << 1):
                divisor = divisor << 1
                tmp2 = tmp2 << 1
            dividend = dividend - divisor
            quotient += tmp2
            divisor = tmp1

        return -quotient if negative else quotient

# if quotient>2**31-1 or quotient<-2**31:
#     quotient = 2**31-1
