# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

# 跳到n与跳到n-1的关系
class Solution:
    def jump(self, nums: List[int]) -> int:
        numsLen = len(nums)
        steps = [0] * numsLen
        numsMax = max(nums)
        for i in range(1, numsLen):
            start = max(0, i - numsMax)
            for j in range(start, i):
                if nums[j] >= (i-j):
                    steps[i] = steps[j] + 1
                    break
        
        return steps[numsLen-1]

# 跳n步最多能跳多远 
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        l, r = 0, nums[0]
        times = 1
        while r < len(nums) - 1:
            times += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            l, r = r, nxt
        
        return times