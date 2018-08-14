'''

Given a matrix consists of 0 and 1,

find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0

Example 2:
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1

Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.

'''

import sys
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(matrix)
        col = len(matrix[0])
        ans = []
        for i in xrange(row):
            ans.append([])
            for j in xrange(col):
                ans[i].append(0)

        queue = []
        for x in xrange(row):
            for y in xrange(col):
                if matrix[x][y] != 0:
                    queue.append((x, y))

        path = 0

        while queue:
            path += 1
            nextQueue = []
            removeQueue = []
            for x, y in queue:
                zero = 0
                dx = [1, 0, 0,-1]
                dy = [0,-1, 1, 0]
                for k in xrange(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < row and 0 <= ny < col and matrix[nx][ny] == 0:
                        zero += 1

                if zero:
                    ans[x][y] = path
                    removeQueue.append((x, y))
                else:
                    nextQueue.append((x, y))

            for x, y in removeQueue:
                matrix[x][y] = 0

            queue = nextQueue
        return ans





class Solution_TLE(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        row = len(matrix)
        col = len(matrix[0])
        ans = []
        for i in xrange(row):
            ans.append([])
            for j in xrange(col):
                ans[i].append(sys.maxint)

        for x in xrange(row):
            for y in xrange(col):
                if matrix[x][y] == 0:
                    self.dfs(matrix, ans, x, y, 0)


        return ans

    def dfs(self, matrix, ans, x, y, path):
        if x > len(matrix) - 1 or x < 0:
            return
        if y > len(matrix[0]) - 1 or y < 0:
            return

        if ans[x][y] <= path:
            return

        if matrix[x][y] == 0:
            path = 0

        ans[x][y] = path

        self.dfs(matrix, ans, x + 1, y, path+1)
        self.dfs(matrix, ans, x - 1, y, path+1)
        self.dfs(matrix, ans, x, y + 1, path+1)
        self.dfs(matrix, ans, x, y - 1, path+1)





matrix = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]

print Solution().updateMatrix(matrix)