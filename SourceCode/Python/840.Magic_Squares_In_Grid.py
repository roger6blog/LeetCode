'''

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row,

column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?

(Each subgrid is contiguous).


Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]

Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15

'''


class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        i = 0
        j = 0
        count = 0
        if row == 3 and col == 3:
            for x in xrange(row):
                for y in xrange(col):
                    if not (10 > grid[i][j] > 0):
                        return 0


        while i + 2 < row:
            # print("[{}][{}]: {}".format(i, j, grid[i][j]))
            j = 0
            while j + 2 < col:
                print("[{}][{}]: {}".format(i, j, grid[i][j]))
                validMatrix = True
                for x in xrange(i, i+2):
                    for y in xrange(j, j+2):
                        if not (10 > grid[x][y] > 0):
                            validMatrix = False
                if not validMatrix:
                    j += 1
                    continue
                if not (10 > grid[i][j] > 0):
                    j += 1
                    continue
                if grid[i + 1][j + 1] != 5:
                    j += 1
                    continue
                if grid[i][j] + grid[i + 1][j] + grid[i + 2][j] == \
                   grid[i][j] + grid[i][j + 1] + grid[i][j + 2] == \
                   grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] == \
                   grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2] == \
                   grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]:
                    count += 1
                j += 1
            i += 1

        return count

matrix = [
    [4,3,8,4],
    [9,5,1,9],
    [2,7,6,2]
]
matrix2 =[
    [10,3,5],
    [1,6,11],
    [7,9,2]
]

matrix3 = [
    [2,7,6,9],
    [9,5,1,6],
    [4,3,8,8],
    [1,4,10,1]
]

matrix4 = [
    [7,0,5],
    [2,4,6],
    [3,8,1]
]

matrix5 = [
    [4,10,1,6],
    [2,5,8,5],
    [9,0,6,4],
    [1,7,2,9]
]


matrix6 = [
    [8,3,8,3,10,7],
    [9,4,5,9,5,0],
    [0,7,0,8,5,5],
    [6,6,5,4,6,2],
    [5,2,10,3,1,9],
    [9,2,6,7,5,2]
]

matrix7 = [
    [4,3,8,4],
    [9,5,1,9],
    [2,7,6,2]
]

matrix8 = [
    [3,2,9,2,7],
    [6,1,8,4,2],
    [7,5,3,2,7],
    [2,9,4,9,6],
    [4,3,8,2,5]
]
print Solution().numMagicSquaresInside(matrix8)

