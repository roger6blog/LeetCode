'''
Level: Easy Tag: [DP]

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.

In how many distinct ways can you climb to the top?


Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:

1 <= n <= 45
'''




'''

假设梯子有n层，那么如何爬到第n层呢，因为每次只能爬1或2步，
那么爬到第n层的方法要么是从第 n-1 层一步上来的，要不就是从 n-2 层2步上来的，
所以递推公式非常容易的就得出了: dp[n] = dp[n-1] + dp[n-2]。

'''


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        # dp[0] 在本題沒有意義 直接為0，
        if n <= 2:
            return n

        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        print(dp[n])

        return dp[n]

    def climbStairs_rec(self, n):
        """
        :type n: int
        :rtype: int
        """

        def rec(n, memo):
            if n in memo:
                return memo[n]

            memo[n] = rec(n-1, memo) + rec(n-2, memo)
            return memo[n]

        memo = {}
        memo[1] = 1
        memo[2] = 2
        ans = rec(n, memo)

        print(ans)
        return ans
n = 2
assert 2 == Solution().climbStairs(n)
n = 3
assert 3 == Solution().climbStairs(n)
n = 5
assert 8 == Solution().climbStairs(n)
assert 8 == Solution().climbStairs_rec(n)