'''
Level: Medium Tag: 2DP -> Optimized to 1DP

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.

The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.



Example 1:

"../../../Material/robot1.jpeg"

Input: obstacleGrid = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]

Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:

"../../../Material/robot2.jpeg"

Input: obstacleGrid = [
    [0,1],
    [0,0]
]
Output: 1


Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.

'''


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1:
            if obstacleGrid[0][0] == 1:
                return 0
            else:
                return 1

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]

        print(dp[m-1][n-1])
        return dp[m-1][n-1]

obstacleGrid = [
    [0,1],
    [0,0]
]
assert 1 == Solution().uniquePathsWithObstacles(obstacleGrid)

obstacleGrid = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
assert 2 == Solution().uniquePathsWithObstacles(obstacleGrid)

obstacleGrid = [[1]]
assert 0 == Solution().uniquePathsWithObstacles(obstacleGrid)

obstacleGrid = [[0]]
assert 1 == Solution().uniquePathsWithObstacles(obstacleGrid)

obstacleGrid = [[1,0]]
assert 0 == Solution().uniquePathsWithObstacles(obstacleGrid)