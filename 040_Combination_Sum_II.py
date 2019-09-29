# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

# index + 1避免重复使用同一个数字，同时使用candidates[i] != candidates[i-1]进行判断
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, -1, [], res)
        return res

    def dfs(self, candidates, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in range(index+1, len(candidates)):
            if candidates[i] > target:
                break
            if i == (index + 1):
                self.dfs(candidates, target-candidates[i], i, path+[candidates[i]], res)
            else:
                if candidates[i] != candidates[i-1]:
                    self.dfs(candidates, target-candidates[i], i, path+[candidates[i]], res)