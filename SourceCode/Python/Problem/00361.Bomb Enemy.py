'''
Level: Medium  Tag: [Matrix], [DP]

Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero),

return the maximum enemies you can kill using one bomb.

The bomb kills all the enemies in the same row and column from the planted point

until it hits the wall since the wall is too strong to be destroyed.


You can only put the bomb at an empty cell.

Example1

Input:
grid =[
     "0E00",
     "E0WE",
     "0E00"
]
Output: 3
Explanation:
Placing a bomb at (1,1) kills 3 enemies

Example2

Input:
grid =[
     "0E00",
     "EEWE",
     "0E00"
]
Output: 2
Explanation:
Placing a bomb at (0,0) or (0,3) or (2,0) or (2,3) kills 2 enemies


'''

class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):


        if grid == None or len(grid) == 0:
            return 0

        row = len(grid)
        col = len(grid[0])
        right = [[0] * col for _ in range(row)]
        down = [[0] * col for _ in range(row)]
        left = [[0] * col for _ in range(row)]
        up = [[0] * col for _ in range(row)]

        # right (left -> right)
        for x in range(row):
            for y in range(col):
                if grid[x][y] != 'W':
                    if grid[x][y] == 'E':
                        right[x][y] = 1
                    if y > 0:
                        right[x][y] += right[x][y-1]

        # down (up -> down)
        for x in range(row):
            for y in range(col):
                if grid[x][y] != 'W':
                    if grid[x][y] == 'E':
                        down[x][y] = 1
                    if x > 0:
                        down[x][y] += down[x-1][y]

        # left (right -> left)
        for x in range(row):
            for y in range(col-1, -1, -1):
                if grid[x][y] != 'W':
                    if grid[x][y] == 'E':
                        left[x][y] = 1
                    if y + 1 < col:
                        left[x][y] += left[x][y+1]

        # up (down -> up)
        for x in range(row-1, -1, -1):
            for y in range(col):
                if grid[x][y] != 'W':
                    if grid[x][y] == 'E':
                        up[x][y] = 1
                    if x + 1 < row:
                        up[x][y] += up[x+1][y]

        ans = 0
        for x in range(row):
            for y in range(col):
                if grid[x][y] == '0':
                    ans = max(ans, right[x][y] + down[x][y] + left[x][y] + up[x][y])

        print(ans)
        return ans


grid =[
     "0E00",
     "E0WE",
     "0E00"
]
Solution().maxKilledEnemies(grid)