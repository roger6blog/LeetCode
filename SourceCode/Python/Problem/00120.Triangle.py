'''
Level: Medium  Tag: [DP]

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally,

if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.


Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11

Example 2:

Input: triangle = [[-10]]
Output: -10


Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-10^4 <= triangle[i][j] <= 10^4


Follow up: Could you do this using only O(n) extra space,
where n is the total number of rows in the triangle?


'''


'''

DP[i][j] = min(DP[i-1][j-1], DP[i-1][j]) + trangle[i][j]

'''

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        # dp[i][j] 代表從0,0 走到i, j的最短路徑值
        dp = [[0] * (i+1) for i in range(n)]

        # 初始值，三角形的左右要初始化
        # 因為他們沒有上面的路徑能到達
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]

        # 轉移方程式 DP[i][j] = min(DP[i-1][j-1], DP[i-1][j]) + trangle[i][j]
        # i,j 這位置是從 i-1,j 或 i-1,j-1 走過來的
        for i in range(2, n):
            for j in range(1, i): # 三角形的matrix 無法走到n,只能走到i
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

        print(min(dp[n-1]))
        return min(dp[n-1])



triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Solution().minimumTotal(triangle)