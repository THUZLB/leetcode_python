# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        neg = True if n < 0 else False
        if neg:
            x = 1/x
            n = -n
        res = 1
        binn = bin(n)[2:]
        for i in binn:
            if i == '1':
                res = res**2 * x
            else:
                res = res**2
                
        return res

# 从低位到高位迭代，需要递增x
class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow