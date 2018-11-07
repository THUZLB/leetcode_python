# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        r = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                target_3 = target - nums[i]
                r_3 = self.sortedThreeSum(nums[i + 1:], target_3)
                #print('target_3=', target_3)
                #print(r_3)
                if r_3 is not None:
                    for list_3 in r_3:
                        tmp = [nums[i]]
                        tmp.extend(list_3)
                        r.append(tmp)
        return r

    def sortedThreeSum(self, nums, target):
        result = []
        for l in range(len(nums) - 2):
            m = l + 1
            r = len(nums) - 1
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            else:
                while m < r:
                    s = nums[l] + nums[m] + nums[r]
                    if s == target:
                        result.append([nums[l], nums[m], nums[r]])
                        while m < r and nums[m] == nums[m + 1]:
                            m += 1
                        while m < r and nums[r] == nums[r - 1]:
                            r -= 1
                        m += 1
                        r -= 1
                    elif s > target:
                        r -= 1
                    else:
                        m += 1
        return result


# test
nums = [-1,-5,-5,-3,2,5,0,4]
solution = Solution()
print(solution.fourSum(nums, -7))
