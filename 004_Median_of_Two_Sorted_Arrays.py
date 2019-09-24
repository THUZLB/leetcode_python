# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        if m == 0:
            mid = (nums2[(n-1)//2] + nums2[n//2])/2
            return mid
        
        iMin = 0
        iMax = m
        h = (m + n + 1)//2
        
        while(iMin <= iMax):
            i = (iMin + iMax) // 2
            j = h - i
            if(i > iMin and nums1[i-1] > nums2[j]): # i值过大
                iMax = i - 1
            elif(i < iMax and nums1[i] < nums2[j - 1]): # i值过小
                iMin = i + 1
            else:
                if i == 0:
                    lMax = nums2[j-1]
                elif j == 0:
                    lMax = nums1[i-1]
                else:
                    lMax = max(nums1[i-1], nums2[j-1])
                if(m+n+1)%2 == 0:
                    return lMax
                
                if i == m:
                    rMin = nums2[j]
                elif j == n:
                    rMin = nums1[i]
                else:
                    rMin = min(nums1[i], nums2[j])
                
                mid = (lMax + rMin)/2
                return mid