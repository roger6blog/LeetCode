'''
Level: Medium  Tag: [DP]

Given a 01 matrix, find the longest line of consecutive 1 in the matrix.

The line could be horizontal, vertical, diagonal or anti-diagonal.


The number of elements in the given matrix will not exceed 10,000.


Example 1:

Input:
  [[0,1,1,0],
   [0,1,1,0],
   [0,0,0,1]]
Output: 3
Explanation: (0,1) (1,2) (2,3)
Example 2:

Input: [[0,0],[1,1]]
Output: 2

'''



class Solution:
    """
    @param M: the 01 matrix
    @return: the longest line of consecutive one in the matrix
    """

    def longestLine(self, M):
        dp = M[:]
        dx = [0, -1, -1]
        dy = [-1, 0, -1]
        dir = []
        for i in range(len(dx)):
            dir.append((dx[i], dy[i]))

        def max_nearby(m, x, y):
            res = 0
            for dx, dy in dir:
                x += dx
                y += dy
                if x < 0 or y < 0 or x >= len(m) or y >= len(m[0]):
                    break
                res = max(res, m[x][y])
            return res

        ans = 0
        for x in range(len(dp)):
            for y in range(len(dp[0])):
                dp[x][y] += max_nearby(dp, x, y)
                ans = max(ans, dp[x][y])

        return ans




matrix = [[0,1,1,0],
   [0,1,1,0],
   [0,0,0,1]]

Solution().longestLine(matrix)