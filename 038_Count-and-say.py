# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

# original solution by THUZLB
# class Solution:
#     def countAndSay(self, n):
#         """
#         :type n: int
#         :rtype: str
#         """
#
#         s = '1'
#         if n == 1:
#             return s
#         else:
#             for i in range(n-1):
#                 s_l = []
#                 j_p = 0
#                 for j in range(len(s)):
#                     if j == len(s) - 1:
#                         if s[j] != s[j_p]:
#                             s_l.append(str(j - j_p))
#                             s_l.append(s[j_p])
#                             s_l.append(s[j])
#                             s_l.append(str(1))
#                         else:
#                             s_l.append(str(j - j_p + 1))
#                             s_l.append(s[j_p])
#                     else:
#                         if j > j_p and s[j] != s[j_p]:
#                             s_l.append(str(j - j_p))
#                             s_l.append(s[j_p])
#                             j_p = j
#                 s = ''.join(s_l)
#
#             return s


# best solution in leetcode, recoded by THUZLB
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(1, n):
            count = 0
            char = None
            s_new = ''
            for x in s:
                if char is None:
                    char = x
                    count = 1
                elif x == char:
                    count += 1
                else:
                    s_new += str(count) + char
                    char = x
                    count = 1
            if char is not None:
                s_new += str(count) + char
            s = s_new

        return s


# test
solution = Solution()
print(solution.countAndSay(5))
