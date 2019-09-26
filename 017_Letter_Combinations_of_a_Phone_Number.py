# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

# 迭代解法
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsDict = {'2':['a', 'b', 'c'], '3':['d', 'e','f'], '4':['g', 'h', 'i'], '5':['j', 'k','l'],\
                      '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        digitsLen = len(digits)
        if digitsLen == 0:
            return []
        elif digitsLen == 1:
            return digitsDict[digits]
        else:
            return [s1 + s2 for s1 in digitsDict[digits[0]] for s2 in self.letterCombinations(digits[1:])]


# 循环解法
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsDict = {'2':['a', 'b', 'c'], '3':['d', 'e','f'], '4':['g', 'h', 'i'], '5':['j', 'k','l'],\
                      '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        
        result = [''] if digits else []
        for d in digits:
            dl = digitsDict[d]
            resultNew = [s1 + s2 for s1 in result for s2 in dl]
            result = resultNew
        
        return result