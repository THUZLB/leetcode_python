# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        # 递归还可以这样，厉害！
        # 可以穷举再判断是否正确
        def generate(A='', left=0, right=0):
            if len(A) == 2 * n:
                result.append("".join(A))
                return
            if left < n:  # 先对左括号递归
                generate(A + '(', left + 1, right)
            if right < left:  # 再对右括号递归
                generate(A + ')', left, right + 1)

        result = []
        generate()
        return result


# best solution in LeetCode
# 简单精髓！
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        print(dp)
        return dp[n]


if __name__ == '__main__':
    solution = Solution()
    n = 3
    print(solution.generateParenthesis(n))
