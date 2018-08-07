'''

Find all possible combinations of k numbers that add up to a number n,

given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]



'''


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        ans = []
        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.combination(k, n, digits, [], ans)
        return ans


    def combination(self, k, n, digits, current, ans):
        if len(current) > k:
            return

        if current:
            s = sum(current)
        else:
            s = 0

        if s > n:
            return
        elif s == n:
            if len(current) != k:
                return

            current.sort()
            ans.append(current)
        else:
            for c, i in enumerate(digits):
                self.combination(k, n, digits[c+1:], current + [i], ans)



k = 3
n = 7
print Solution().combinationSum3(k, n)