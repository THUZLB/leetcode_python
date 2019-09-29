# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

# maxL和maxR可以递推
class Solution:
    def trap(self, height: List[int]) -> int:
        heightLen = len(height)
        maxL = height[:]
        maxR = height[:]

        for i in range(1, heightLen):
            if height[i] < maxL[i-1]:
                maxL[i] = maxL[i-1]

        for i in range(heightLen-2, -1, -1):
            if height[i] < maxR[i+1]:
                maxR[i] = maxR[i+1]

        ans = 0
        for i in range(1, heightLen - 1):
            heightMin = min(maxL[i], maxR[i])
            ans += heightMin - height[i]

        return ans

# 使用两个指针避免两次循环
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        lmax = 0
        rmax = 0
        ans = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= lmax:
                    lmax = height[l]
                else:
                    ans += lmax - height[l]
                l += 1
            else:
                if height[r] >= rmax:
                    rmax = height[r]
                else:
                    ans += rmax - height[r]
                r -= 1
        
        return ans