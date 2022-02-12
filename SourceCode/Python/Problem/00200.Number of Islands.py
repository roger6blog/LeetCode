'''
Level: Medium   Tag: [Matrix], [DFS]

Given a 2d grid map of '1's (land) and '0's (water),
count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'

'''

class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])
        count = 0
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] == '1':
                    self.dfs(grid, row, col, i, j)
                    count += 1
        return count

    def dfs(self, grid, row, col, x, y):
        if grid[x][y] == '0':
            return
        grid[x][y] = '0'

        if x != 0:
            self.dfs(grid, row, col, x - 1, y)
        if x != row - 1:
            self.dfs(grid, row, col, x + 1, y)
        if y != 0:
            self.dfs(grid, row, col, x, y - 1)
        if y != col - 1:
            self.dfs(grid, row, col, x, y + 1)














    def numIslands2(self, grid):

        def change_zero_rec(grid, x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return

            if grid[x][y] == '0':
                return

            grid[x][y] = '0'

            # 沒在這裡做判斷而在function開頭做
            # code比較精簡，但是效能較差，因為要多call幾次遞迴
            change_zero_rec(grid, x+1, y)
            change_zero_rec(grid, x-1, y)
            change_zero_rec(grid, x, y+1)
            change_zero_rec(grid, x, y-1)

        if len(grid) == 0 or not grid:
            return 0

        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    change_zero_rec(grid, x, y)
                    count += 1

        return count



grid = """11000
11000
00100
00011"""

grid = [list(line) for line in grid.splitlines()]
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(Solution().numIslands(grid))
grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
print(Solution().numIslands2(grid))