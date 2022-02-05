'''
Level: Medium  Tag: [Matrix]


The island is partitioned into a grid of square cells.

You are given an m x n integer matrix heights where heights[r][c] represents the height
above sea level of the cell at coordinate (r, c).

The island receives a lot of rain,
and the rain water can flow to neighboring cells directly north, south, east, and west
if the neighboring cell's height is less than or equal to the current cell's height.

Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water
can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.


=============  Older Description  ===============


Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent,

the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches
the right and bottom edges.

Water can only flow in four directions (up, down, left, or right)
from a cell to another one with height equal or lower.


Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

"../../../Material/waterflow-grid.jpg"

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).


Example 2:

Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]


Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 10^5

'''




'''

跟之前那道 Surrounded Regions 很类似, 都是换一个方向考虑问题
既然从每个点向中间扩散会 TLE, 那么我们就把所有边缘点当作起点开始遍历搜索, 然后标记能到达的点为 true
分别标记出 pacific 和 atlantic 能到达的点, 那么最终能返回的点就是二者均为 true 的点。



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
        pacific = set()
        atlantic = set()

        def dfs(x, y, matrix, visited, lower_area):
            row = len(matrix)
            col = len(matrix[0])
            if x < 0 or x >= row or y < 0 or y >= col:
                return

            if (x, y) in visited:
                return

            if matrix[x][y] < lower_area:
                return

            visited.add((x, y))

            dfs(x+1, y, matrix, visited, matrix[x][y])
            dfs(x-1, y, matrix, visited, matrix[x][y])
            dfs(x, y+1, matrix, visited, matrix[x][y])
            dfs(x, y-1, matrix, visited, matrix[x][y])

        for i in range(col):
            dfs(0, i, matrix, pacific, -1)      # 太平洋左上角到右上角
            dfs(row-1, i, matrix, atlantic, -1) # 大西洋左下角到右下角

        for i in range(row):
            dfs(i, 0, matrix, pacific, -1)      # 太平洋左上角到左下角
            dfs(i, col-1, matrix, atlantic, -1) # 大西洋右上角到右下角

        ans = list(pacific & atlantic)
        print(ans)
        return ans





sea = [
 [1, 2, 2, 3, 5],
 [3, 2, 3, 4, 4],
 [2, 4, 5, 3, 1],
 [6, 7, 1, 4, 5],
 [5, 1, 1, 2, 4]
]
print(Solution().pacificAtlantic(sea))
# print [0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]

print(MySolution().pacificAtlantic(sea))