'''
Level: Medium Tag: 2DP

Given a m x n grid filled with non-negative numbers,

find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.



Example 1:

"../../../Material/minpath.jpg"

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100


'''




'''

設DP[i][j] 為走到grid[i][j] 的總和
那DP[m][n] 為 do[m-1][n], dp[m][n-1]兩者的最小值加上grid[m][n]
所以轉移方程為 dp[m][n] = min(do[m-1][n], dp[m][n-1]) + grid[m][n]

'''



class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # 定義已知的狀況
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        print(dp[m-1][n-1])

        return dp[m-1][n-1]


grid = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
]

Solution().minPathSum(grid)