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

1.定义状态数组:f[i]表示和为i当前最少平方个数
2.初始化f[i] = i，因为对于和为i最多有i个平方和且每个平方都是1
3.对于每一个i，对j循环直到j * j > i，
每次一次循環都把f[i]和f[i - j * j] + 1进行比较，如果发现更小值,更改f[i] = f[i - j * j] + 1

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

a = Solution().numSquares(111)
print a