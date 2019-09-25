# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        if strX == strX[::-1]:
            return True
        else:
            return False