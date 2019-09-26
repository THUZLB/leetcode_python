# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        sDict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in sDict.values():
                stack.append(char)
            elif char in sDict.keys():
                if stack == [] or sDict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []