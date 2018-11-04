# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

# original solution, but timeout
# class Solution:
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#
#         r = []
#         for i in range(len(nums) - 2):
#             for j in range(i + 1, len(nums) - 1):
#                 if (0 - nums[i] - nums[j]) in nums[j + 1:]:
#                     l = [nums[i], nums[j], 0 - nums[i] - nums[j]]
#                     l.sort()
#                     if l not in r:
#                         r.append(l)
#
#         return r


# new solution
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        r = []
        nums.sort()
        for start in range((len(nums) - 2)):
            if start > 0 and nums[start] == nums[start - 1]:
                continue
            else:
                middle, end = start + 1, len(nums) - 1
                while middle < end:
                    s = nums[start] + nums[middle] + nums[end]
                    if s == 0:
                        r.append([nums[start], nums[middle], nums[end]])

                        # only find a solution then duplicate triplets should be eliminated
                        while middle < end and nums[middle] == nums[middle + 1]:
                            middle += 1
                        while middle < end and nums[end] == nums[end - 1]:
                            end -= 1
                        middle += 1
                        end -= 1
                    elif s > 0:
                        end -= 1
                    else:
                        middle += 1
        return r


# test
nums = [-1, 0, 1, 2, -1, -4]
solution = Solution()
print(solution.threeSum(nums))
