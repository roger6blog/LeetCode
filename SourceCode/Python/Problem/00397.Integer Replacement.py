'''
Level: Medium  Tag: [Math]


Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.



Example 1:

Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1

Example 2:

Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1

Example 3:

Input: n = 4
Output: 2


Constraints:

1 <= n <= 2^31 - 1


'''

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {}
        def rec(n):
            if n in dp:
                return dp[n]
            if n == 1:
                ans = 0

            elif n & 1 == 1: # 判斷奇偶
                ans = min(rec(n+1), rec(n-1)) + 1
            else:
                ans = rec(n//2)+1

            dp[n] = ans
            return ans

        rec(n)
        print(dp[n])
        return dp[n]

n = 100
Solution().integerReplacement(n)