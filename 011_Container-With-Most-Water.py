# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_container = 0
        l = 0
        r = len(height) - 1
        while l < r:
            container = (r - l) * min(height[l], height[r])
            max_container = max(max_container, container)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_container

# test
height = [1,8,6,2,5,4,8,3,7]
solution = Solution()
print(solution.maxArea(height))
