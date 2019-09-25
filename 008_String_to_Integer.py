# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

class Solution:
    def myAtoi(self, str: str) -> int:
        sign = 1
        signOnly = True
        numTrue = True
        numLast = False
        strLen = len(str)
        if strLen == 0:
            return 0
        i = 0
        res = 0
        while i < strLen and numTrue is True:
            if str[i] == ' ':
                if numLast:
                    numTrue = False
            elif str[i] == '-' and signOnly is True:
                if numLast:
                    numTrue = False
                else:
                    sign = -1
                    signOnly = False
                    numLast = True
            elif str[i] == '+' and signOnly is True:
                if numLast:
                    numTrue = False
                else:
                    signOnly = False
                    numLast = True
            elif str[i] in '0123456789':
                res = res*10 + int(str[i])
                numLast = True
            else:
                numTrue = False
            i += 1
        
        res = res * sign
        
        maxI = pow(2,31) - 1
        minI = -maxI - 1
        
        if res > maxI:
            return maxI
        elif res < minI:
            return minI
        else:
            return res