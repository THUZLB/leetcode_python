# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        minc = min(candidates)
        if target < minc:
            return []
        elif target in candidates:
            ans = [[target]]
            for c in candidates:
                ansNew = [[c] + i for i in self.combinationSum(candidates, target-c)]
                for an in ansNew:
                    an.sort()
                    if an not in ans:
                        ans += [an]
            return ans
        else:
            ans = []
            for c in candidates:
                ansNew = [[c] + i for i in self.combinationSum(candidates, target-c)]
                for an in ansNew:
                    an.sort()
                    if an not in ans:
                        ans += [an]
            return ans


# 注意index的作用，取了数字nums[i]，下次就只能从nums[i]开始
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in range(index, len(nums)):
            if nums[i] > target:
                break
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)