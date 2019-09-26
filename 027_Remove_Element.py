# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        numsLen = len(nums)
        i = 0
        
        while i < numsLen:
            if nums[i] == val:
                nums[i] = nums[numsLen - 1]
                numsLen -= 1
            else:
                i += 1
        
        return numsLen