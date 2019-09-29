# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

# 注意while循环，防止交换后当前位置不符合要求
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numsLen = len(nums)
        for i in range(numsLen):
            loc = nums[i]-1
            while 0 < nums[i] <= numsLen and nums[loc] != nums[i]:
                nums[i], nums[loc] = nums[loc], nums[i]
                loc = nums[i]-1
        for i in range(numsLen):
            if nums[i] != (i+1):
                return (i+1)
        
        return (numsLen+1)   