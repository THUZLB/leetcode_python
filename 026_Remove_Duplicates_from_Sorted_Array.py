# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

# 使用list.remove()非常慢，直接移动，并返回正确长度就好了

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numsNewLen = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[numsNewLen]:
                numsNewLen += 1
                if i > numsNewLen:
                    nums[numsNewLen] = nums[i]
        
        numsNewLen += 1
        
        return numsNewLen