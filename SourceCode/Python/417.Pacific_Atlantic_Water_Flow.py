'''

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent,

the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).


'''
import sys
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(matrix)
        col = len(matrix[0])

        ans = []
        pacific = [[False for _ in xrange(col)] for _ in xrange(row)]
        atlantic = [[False for _ in xrange(col)] for _ in xrange(row)]

        for i in xrange(row):
            self.dfs(matrix, pacific, -sys.maxint - 1, i, 0)
            self.dfs(matrix, atlantic, -sys.maxint - 1, i, col - 1)

        for j in xrange(col):
            self.dfs(matrix, pacific, -sys.maxint - 1, 0, j)
            self.dfs(matrix, atlantic, -sys.maxint - 1, row - 1, j)

        for x in xrange(row):
            for y in xrange(col):
                if pacific[x][y] and atlantic[x][y]:
                    ans.append([x, y])

        return ans

    def dfs(self, matrix, visited, pre, x, y):
        if x >= len(matrix) or x < 0:
            return
        if y >= len(matrix[0]) or y < 0:
            return

        if visited[x][y] == True:
            return

        if matrix[x][y] < pre:
            return

        visited[x][y] = True
        self.dfs(matrix, visited, matrix[x][y], x + 1, y)
        self.dfs(matrix, visited, matrix[x][y], x - 1, y)
        self.dfs(matrix, visited, matrix[x][y], x, y + 1)
        self.dfs(matrix, visited, matrix[x][y], x, y - 1)


class MySolution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        row = len(matrix)
        col = len(matrix[0])
        ans = []
        for x in xrange(row):
            for y in xrange(col):
                orgPoint = [x, y ,False, False, matrix[x][y]]
                self.dfs(matrix, x, y, ans, orgPoint)

        return ans

    def dfs(self, matrix, x, y, ans, orgPoint):
        if x >= len(matrix) or x < 0:
            return
        if y >= len(matrix[0]) or y < 0:
            return

        if matrix[x][y] == -1:
            return

        if matrix[x][y] > orgPoint[-1]:
            return

        if x == 0 or y == 0:
            orgPoint[2] = True

        if x == len(matrix) - 1 or y == len(matrix[0]) - 1:
            orgPoint[3] = True


        if orgPoint[2] == True and orgPoint[3] == True:
            if [orgPoint[0], orgPoint[1]] not in ans:
                ans.append([orgPoint[0], orgPoint[1]])
            return
        # temp2 = orgPoint[-1]
        # orgPoint[-1] = matrix[x][y]
        temp = matrix[x][y]
        matrix[x][y] = -1

        self.dfs(matrix, x + 1, y, ans, orgPoint)
        self.dfs(matrix, x - 1, y, ans, orgPoint)
        self.dfs(matrix, x, y + 1, ans, orgPoint)
        self.dfs(matrix, x, y - 1, ans, orgPoint)


        matrix[x][y] = temp
        # orgPoint[-1] = temp2



sea = [
 [1, 2, 2, 3, 5],
 [3, 2, 3, 4, 4],
 [2, 4, 5, 3, 1],
 [6, 7, 1, 4, 5],
 [5, 1, 1, 2, 4]
]
print Solution().pacificAtlantic(sea)
print [0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]