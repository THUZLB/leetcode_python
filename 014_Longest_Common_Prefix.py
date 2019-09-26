# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strsLen = len(strs)
        if strsLen == 0:
            return ''
        for i in range(len(strs[0])):
            j = 1
            while j < strsLen:
                if i == len(strs[j]) or strs[0][i] != strs[j][i]:
                    return strs[0][0:i]
                else:
                    j += 1
        return strs[0]