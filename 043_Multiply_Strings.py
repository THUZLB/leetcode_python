# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1Len = len(num1)
        num2Len = len(num2)
        ans = [0] * (num1Len + num2Len)
        
        for i in range(num1Len):
            carry = 0
            for j in range(num2Len):
                nsum =  ans[num1Len+num2Len-i-j-1] + (ord(num1[num1Len-i-1])-48) * (ord(num2[num2Len-j-1])-48) + carry
                # nsum =  ans[num1Len+num2Len-i-j-1] + int(num1[num1Len-i-1]) * int(num2[num2Len-j-1]) + carry
                carry = nsum // 10
                ans[num1Len + num2Len - i - j -1] = nsum % 10
            ans[num1Len - i - 1] = carry
        
        res = ''.join([str(i) for i in ans])
        res = res.lstrip('0')
        if not res:
            res = '0'
            
        return res