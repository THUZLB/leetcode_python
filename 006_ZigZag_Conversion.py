# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        sLen = len(s)
        if numRows >= sLen or numRows == 1:
            return s
        modulo = 2 * numRows - 2
        result = []
        for i in range(numRows):
            j = i
            while j < sLen:
                result.append(s[j])
                if i != 0 and i != (numRows - 1) and (j+modulo-i-i) < sLen:
                    result.append(s[j+modulo-i-i])
                j += modulo

        return ''.join(result)

# 使用方向的解法
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)