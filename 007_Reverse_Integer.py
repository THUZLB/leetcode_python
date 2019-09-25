# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        minX = -pow(2, 31)
        maxX = -minX - 1
        xStr = str(x)
        xStrR = []
        Zero = True
        
        if x < 0:
            xStrR.append('-')
            for i in range(len(xStr)-1, 0, -1):
                if xStr[i] == '0' and Zero:
                    continue
                else:
                    xStrR.append(xStr[i])
                    Zero = False
        else:
            for i in range(len(xStr)-1, -1, -1):
                if xStr[i] == '0' and Zero:
                    continue
                else:
                    xStrR.append(xStr[i])
                    Zero = False
        
        xStrR = ''.join(xStrR)
        xR = int(xStrR)
        
        if minX <= xR <= maxX:
            return xR
        else:
            return 0

# 求模解法
class Solution:
    def reverse(self, x: int) -> int:
        minX = -pow(2, 31)
        maxX = -minX - 1
        res = 0
        sigh = 1 if x >= 0 else -1
        x = abs(x)
        while x != 0:
            res = res*10 + x%10
            x = x // 10
        
        res = sigh * res
        
        if minX <= res <= maxX:
            return res
        else:
            return 0