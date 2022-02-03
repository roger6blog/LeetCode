'''
Level: Medium  Tag:[Math]

Given an integer n, break it into the sum of k positive integers, where k >= 2,

and maximize the product of those integers.

Return the maximum product you can get.



Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 x 1 = 1.

Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 x 3 x 4 = 36.


Constraints:

2 <= n <= 58
'''

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2 or n ==3:
            return n - 1

        ans = 1
        while n > 4:
            ans *= 3
            n -= 3

        ans *= n
        print(ans)
        return ans



n = 10
Solution().integerBreak(n)
n = 58
Solution().integerBreak(n)