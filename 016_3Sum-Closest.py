# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        from bisect import bisect
        nums.sort()

        diff = None
        r = None
        r_sum = None
        for start in range(len(nums) - 2):
            if start > 0 and nums[start] == nums[start - 1]:
                continue
            else:
                end = len(nums) - 1
                while end > (start + 1):
                    diff_target = target - nums[start] - nums[end]
                    if diff_target in nums[start + 1:end]:
                        r = [nums[start], diff_target, nums[end]]
                        r_sum = target
                        return r_sum
                    else:
                        index_targrt = bisect(nums[start + 1:end], diff_target)

                        if index_targrt == 0:
                            diff_actual = target - nums[start] - nums[start + 1] - nums[end]
                            r0 = [nums[start], nums[start + 1], nums[end]]
                        elif index_targrt == end - start - 1:
                            diff_actual = target - nums[start] - nums[end - 1] - nums[end]
                            r0 = [nums[start], nums[end - 1], nums[end]]
                        else:
                            diff_actual_1 = target - nums[start] - nums[start + index_targrt] - nums[end]
                            diff_actual_2 = target - nums[start] - nums[start + index_targrt + 1] - nums[end]
                            if abs(diff_actual_1) < abs(diff_actual_2):
                                diff_actual = diff_actual_1
                                r0 = [nums[start], nums[start + index_targrt], nums[end]]
                            else:
                                diff_actual = diff_actual_2
                                r0 = [nums[start], nums[start + index_targrt + 1], nums[end]]

                        if diff is None:
                            diff = diff_actual
                            r = r0
                        else:
                            if abs(diff_actual) < abs(diff):
                                diff = diff_actual
                                r = r0
                    end -= 1

        # print(r)
        r_sum = sum(r)
        return r_sum


# test
nums = [1, 1, -1, -1, 3]
solution = Solution()
print(solution.threeSumClosest(nums, -1))
