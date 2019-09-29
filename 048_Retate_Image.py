# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            l = 0
            r = n-1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1
                r -= 1

# 此解法空间复杂度非O(1)
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[::] = zip(*matrix[::-1])