# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        strLen = len(s)
        strDict = {}
        subLenMax = 0
        start = 0
        for i in range(strLen):
            if s[i] in strDict and strDict[s[i]] >= start:
                subLenMax = max(subLenMax, i-strDict[s[i]])
                start = strDict[s[i]] + 1
            else:
                subLenMax = max(subLenMax, i-start+1)
            strDict[s[i]] = i
        
        return subLenMax