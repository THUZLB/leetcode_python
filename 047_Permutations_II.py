# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

# 在n-1个的情况上插入，判断是否重复
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        length = 0
        for n in nums:
            new_ans = []
            length += 1
            for l in ans:
                for i in range(length):
                    new_ans.append(l[:i]+[n]+l[i:])
                    if i<len(l) and l[i]==n: break              #handles duplication
            ans = new_ans
        
        return ans