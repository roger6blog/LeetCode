'''

Given an integer matrix,
find the length of the longest increasing path.

From each cell,
you can either move to four directions: left, right, up or down.
You may NOT move diagonally or move outside of the boundary
(i.e. wrap-around is not allowed).

Example 1:

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6].
Moving diagonally is not allowed.


'''

import os


class Solution(object):
    def __init__(self):
        self.longestpath = 1
        self.currx = 0
        self.curry = 0

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0

        row = len(matrix)
        col = len(matrix[0])

        for x in xrange(row):
            for y in xrange(col):
                visited = []
                print "======"
                self.dfs(row, col, x, y, matrix, visited)
        return self.longestpath

    def dfs(self, row, col, x, y, matrix, visited):
        if x >= row or y >= col or x < 0 or y < 0:
            return
        print("Start from matrix[{}][{}] = {}".format(x, y, matrix[x][y]))


        if len(visited) > 1:
            if visited[-1].keys()[0][0] != x and visited[-1].keys()[0][1] != y:
                return



        if visited != []:
            if matrix[x][y] <= visited[-1].values()[0]:
                print("matrix[{}][{}] = {} <= {}".format(x, y, matrix[x][y], visited[-1]))
                return

        visited.append({(x, y):matrix[x][y]})

        self.longestpath = max(self.longestpath, len(visited))
        print self.longestpath, visited

        self.dfs(row, col, x, y + 1, matrix, visited)
        self.dfs(row, col, x, y - 1, matrix, visited)
        self.dfs(row, col, x + 1, y, matrix, visited)
        self.dfs(row, col, x - 1, y, matrix, visited)

        visited.pop()

    def longestIncreasingPath2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0

        def longestpath(matrix, i, j, max_lengths):
            if max_lengths[i][j]:
                return max_lengths[i][j]

            max_depth = 0
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for d in directions:
                x, y = i + d[0], j + d[1]
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] < matrix[i][j]:
                    max_depth = max(max_depth, longestpath(matrix, x, y, max_lengths))
            max_lengths[i][j] = max_depth + 1
            return max_lengths[i][j]

        res = 0
        max_lengths = [[0 for _ in xrange(len(matrix[0]))] for _ in xrange(len(matrix))]
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                res = max(res, longestpath(matrix, i, j, max_lengths))

        return res
a = [
    [9,9,4],
    [6,6,8],
    [2,1,1]
]

b = [
    [3,4,5],
    [3,2,6],
    [2,2,1]
]

c = [
    [6,8],
    [7,2]
]


d = [
    [7,7,5],
    [2,4,6],
    [8,2,0]
]

e = [[1,4,7,9],
     [0,3,8,5],
     [3,6,0,6],
     [1,4,5,6]
]


f = [
    [7,6,1,1],
    [2,7,6,0],
    [1,3,5,1],
    [6,6,3,2]
]
print Solution().longestIncreasingPath(f)