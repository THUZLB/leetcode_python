# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, num in enumerate(nums):
            if (target-num) in table:
                return [i, table[target-num]]
            else:
                table[num] = i