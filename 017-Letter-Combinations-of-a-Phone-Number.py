# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype
        """

        import itertools

        if not digits:
            return []

        digit = range(2, 10)
        letters = ('abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')
        dict_map = {str(a): b for a, b in zip(digit, letters)}

        iter_map = (dict_map[d] for d in digits)
        result = list(set(''.join(x) for x in itertools.product(*iter_map)))

        return result


# best solution in LeetCode
class Solution:
    def combine(self, s1, s2):
        return [x + y for x in s1 for y in s2]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        d = {'2': list('abc'),
             '3': list('def'),
             '4': list('ghi'),
             '5': list('jkl'),
             '6': list('mno'),
             '7': list('pqrs'),
             '8': list('tuv'),
             '9': list('wxyz')}
        res = ['']
        for c in digits:
            res = self.combine(res, d[c])
        return res


if __name__ == '__main__':
    solution = Solution()
    digits = '23'
    print(solution.letterCombinations(digits))
