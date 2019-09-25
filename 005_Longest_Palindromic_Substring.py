# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

class Solution:
    def longestPalindrome(self, s: str) -> str:
        strLen = len(s)
        if strLen == 0:
            return ''
        
        resTable = [[0] * strLen for i in range(strLen)]
        
        maxLen = 1
        result = s[0]
        for i in range(strLen):
            resTable[i][i] = 1
            
            if i < (strLen-1) and s[i] == s[i+1]:
                resTable[i][i+1] = 1
                if 2 > maxLen:
                    maxLen = 2
                    result =s[i:i+2]
        
        for l in range(3, strLen+1):
            for j in range(strLen-l+1):
                if s[j]==s[j+l-1] and resTable[j+1][j+l-2] == 1:
                    resTable[j][j+l-1] = 1
                    if l > maxLen:
                        maxLen = l
                        result = s[j:j+l]
        
        return result

# Manacher马拉车算法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        strLen = len(s)
        if strLen == 0:
             return ''
        
        sNewList = ['$','#']

        for i in range(strLen):
            sNewList.append(s[i])
            sNewList.append('#')
        sNewList.append('\0')

        strLenNew = 2 * strLen + 3
        maxRight = 0
        maxRLoc = 0
        R = [0] * strLenNew

        for i in range(strLenNew-1):
            R[i] = min(R[2*maxRLoc-i], maxRight-i) if maxRight > i else 1
            while sNewList[i + R[i]] == sNewList[i - R[i]]:
                R[i] += 1
            if (i + R[i] > maxRight):
                maxRight = i + R[i]
                maxRLoc = i

        maxR = max(R)
        maxLoc = R.index(maxR)
        
        sFind = sNewList[maxLoc-maxR+1:maxLoc+maxR]
        sFind = ''.join(sFind).replace('#', '')
        
        return sFind
