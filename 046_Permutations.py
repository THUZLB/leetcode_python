# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permute_inner(res, nums):
            if not nums:
                return res

            res_inner = []
            for num in nums:
                res_inner += permute_inner([i+[num] for i in res], list(set(nums)-set([num])))

            return res_inner
        
        result = permute_inner([[]], nums)
        
        return result

# 比较简洁的写法
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        lev, avail, lev_node = 0, nums, []
        N = len(nums)
        def dfs(lev, avail, lev_node):
            if lev == N:
                res.append(lev_node)
                return
            for i in range(len(avail)):
                dfs(lev+1, avail[:i]+avail[i+1:], lev_node+[avail[i]])
        
        dfs(lev, avail, lev_node)
        return(res)