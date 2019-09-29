# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strDict = {}
        for s in strs:
            sl = list(s)
            sl.sort()
            ssort = ''.join(sl)
            if ssort in strDict:
                strDict[ssort].append(s)
            else:
                strDict[ssort] = [s]
        
        return list(strDict.values())
        
# 也可以对每个字母进行计数，比较计数是否相同