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
        dp = [[0] * (len(M[0])+1) for _ in range(len(M)+1)]
        dx = [0, -1, -1, -1]
        dy = [-1, 0, -1,  1]
        dir = []
        for i in range(len(dx)):
            dir.append((dx[i], dy[i]))

        def max_nearby(m, x, y):
            res = 0
            for dx, dy in dir:
                new_x = x + dx
                new_y = y + dy
                if new_x < 0 or new_y < 0 or new_x >= len(m) or new_y >= len(m[0]):
                    continue
                if m[new_x][new_y] == 0:
                    continue
                res = max(res, m[x][y] + m[new_x][new_y])
            return res

        ans = 0
        for x in range(len(M)):
            for y in range(len(M[0])):
                if M[x][y] != 0:
                    dp[x][y] = M[x][y] + max_nearby(M, x, y)
                    ans = max(ans, dp[x][y])

0        return ans




# matrix = [[0,1,1,0],
#    [0,1,1,0],
#    [0,0,0,1]]

# Solution().longestLine(matrix)


matrix = [
    [0,1,1,0],
    [0,1,1,0],
    [0,0,0,1]
    ]
assert 3 == Solution().longestLine(matrix)

matrix = [
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,1,0]
    ]
# Output
# 1
# Expected
# 5
Solution().longestLine(matrix)