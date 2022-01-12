'''
Level: Medium Level: DP

Given a positive integer n,

find the least number of perfect square numbers

(for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Constraints:

1 <= n <= 10^4
'''




'''

动态规划

1.定义状态数组:f[i]表示和为i当前最少平方个数  f[i]表示i最少能被几个完全平方数来表示
2.初始化f[i*i] = 1，因为对于和为i平方的數字來說 只會有一個最小表示的結果，就是f[i*i] = 1，這個1就是i自己
3.對於其他不是平方數的i，我們要找出一個j, 使其j*j的數字最大  但是又不能超過i，即 j*j < i,
這時候的f[i]就會變成 f[i-j*j]+1 如果沒有的話 f[i]就還是f[i]+1
因為無法確定這個j為何，所以不能確定i和j的關係，無法直接用一個i迴圈解決

'''





class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {}
        y = 1
        while y * y <= n:
            dp[y * y] = 1
            y += 1
        for x in range(1, n):
            y = 1
            while x + y * y <= n:
                if x + y * y not in dp or dp[x] + 1 < dp[x + y * y]:
                    dp[x + y * y] = dp[x] + 1
                y += 1
        return dp[n]
















    def numSquares2(self, n):
        """
        :type n: int
        :rtype: int
        """
        from sys import maxint
        dp = [maxint] * (n+1)

        i = 1
        while i*i <= n:
            dp[i*i] = 1
            i += 1

        # 用For會TLE
        # for i in range(n+1):
        #     for j in range(n):
        #         if j*j <= i:
        #             dp[i] = min(dp[i], dp[i - j*j] + 1)

        for i in range(n+1):
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                j += 1
        print(dp[n])
        return dp[n]










a = Solution().numSquares(111)
print(a)


Solution().numSquares2(12)
Solution().numSquares2(111)