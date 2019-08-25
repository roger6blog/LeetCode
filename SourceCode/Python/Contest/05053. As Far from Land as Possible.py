'''

5053. As Far from Land as Possible

Difficulty: Medium
Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.



Example 1:



Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation:
The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:



Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation:
The cell (2, 2) is as far as possible from all the land with distance 4.


Note:

1 <= grid.length == grid[0].length <= 100
grid[i][j] is 0 or 1


'''
class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        waters = []
        lands = []
        for j in range(n):
            for i in range(n):
                if grid[i][j] == 1:
                    lands.append((i, j))
                elif grid[i][j] == 0:
                    waters.append((i, j))
                else:
                    return -1

        if len(waters) == 0 or len(lands) == 0:
            return -1

        max_n_dis = 0
        for w in waters:
            n_dis = min([abs(w[0]-l[0])+abs(w[1]-l[1]) for l in lands])
            max_n_dis = max(max_n_dis, n_dis)

        return max_n_dis


input = [[1,0,0],[0,0,0],[0,0,0]]
input2 = [[1,1,1,0,1,1,0,1,0,0,1,1,0,1,0,1,1,1,1,0,1,0,1,1,0,1,1,0,0,0,1,0,0,1,1,0,0,1,0,0,0,1,1,0,1,1,0,0,1,0,1,0,1,1,1,0,0,1,0,0,1,0,0,0,0,1,0,1,0,1,1,1,0,0,1,1,0,0,1,1],[0,0,0,1,1,0,1,1,1,0,0,1,0,1,0,1,0,0,0,0,1,1,0,1,0,1,1,0,0,0,1,1,0,0,1,0,1,0,1,0,0,0,1,1,1,0,1,0,1,0,0,1,0,0,1,1,1,0,0,0,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1],[0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,1,0,1,1,0,0,1,1,1,1,0,1,0,0,1,0,0,1,1,0,1,1,1,1,0,0,1,0,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,0,0,0],[0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,1,1,0,0,1,1,1,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,1,0,0,1,0,1,1,1,1,1,0,1,0,0,1,0,0,1,1,0,0,0,1,1,0,1,1,1,0,0,0,0,0,0,1,1,0,0,1,1],[1,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,0,1,0,1,1,1,1,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,1,1,0,1,1,0,1,1,1,0,0,0,0,1,1,1,0,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0,1,0],[0,1,0,0,0,0,0,0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1,1,0,1,0,1,0,0,0,1,0,1,0,0,1,0,1,1,0,0,0,0,1,0,0,1,1,0,0,1,1,1,0,0,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1],[1,1,0,1,1,1,0,0,1,1,1,1,1,0,0,0,0,1,0,1,1,1,0,0,0,0,0,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,0,0,1,0,0,0,0,0,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,0,0,1,1,0,0,1,0,0,1,0,0,1,0,1],[1,1,0,0,1,1,0,1,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,1,1,0,0,1,0,0,1,1,0,1,1,1,1,0,0,0,1,1,0,1,1,0,0,0,1,1,1,0,0,1,1],[1,0,0,1,1,1,1,1,1,1,0,1,0,0,1,0,1,0,0,1,1,1,1,0,0,1,0,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,0,1,1,0,0],[1,1,0,1,1,1,0,0,1,0,1,0,1,1,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1,0,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,0,1,1,1,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1,0,1,1,0,0,0,1,0,1,1,0,0],[0,1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0,1,0,1,1,0,1,1,1,1,1,1,0,1,1,1,1,0,1,0,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,0,1,1,0,0,1,0,1,1,1,0,0,1,1,0],[1,1,0,0,0,1,0,0,1,1,0,1,1,0,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,1,1,1,1,1,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,1,1,0,1,0,0,1,1,0,0,0,1,1,1],[1,0,0,0,0,1,1,1,1,1,0,1,1,0,0,1,1,1,1,0,1,1,1,0,0,0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,0,1,0,1,0,0,0,1,1,0,1,0,0,0,0,0,1,1,0,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1],[0,1,0,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,0,0,1,0,1,1,0,1,1,0,1,1,1,1,0,0,1,1,0,0,1,1,1,0,1,0,0,1,0,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1,1,0,1],[0,1,0,1,0,1,0,1,1,1,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0,1,1,1,0,0,0,1,0,0,0,0,0,1,1,1,1,1,0,1,0,0,1,0,1,1,0,1,0,1,1,0],[0,0,1,1,0,1,0,1,1,0,0,1,1,0,1,0,1,0,0,1,0,1,1,0,0,0,1,1,0,0,0,1,0,1,0,0,1,0,1,0,1,1,0,1,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,0,0,1],[1,1,0,0,0,1,1,0,0,1,0,0,1,1,0,0,0,1,1,1,0,1,0,1,0,1,1,1,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,1,1,1,1,0,1,1,0,1,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,1,1,1,0],[0,1,1,0,0,1,0,1,0,0,1,0,0,1,0,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,0,1,0,0,0,0,1,0,1,0,1,1,0,0,0,0,1,0,1,0,1,1,0,0],[0,0,1,0,1,0,0,0,1,1,1,1,0,1,1,0,0,0,1,1,1,0,0,1,0,1,0,1,1,1,0,1,1,1,1,0,0,0,1,1,0,1,1,0,0,0,1,1,1,0,0,0,1,0,0,0,1,0,1,1,1,1,0,1,0,1,0,1,1,0,0,1,0,0,0,1,0,0,1,1],[0,0,1,1,0,1,0,1,0,1,1,1,0,0,1,1,0,0,1,1,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,0,0,0,1,1,1,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,1,0,0,1,1,0,1,0,0],[0,1,1,0,1,1,0,1,1,1,0,1,1,1,1,0,1,0,0,1,1,1,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0,1,0,0,0,1,0,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1,0,1,1,0,1,1,1,1,0,1,1,1,0],[0,0,0,0,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,1,0,0,0,0,1,1,1,1,1,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0],[1,1,1,0,0,0,0,1,1,1,0,1,1,0,0,1,1,1,1,0,0,0,0,1,0,0,1,0,0,0,1,1,1,0,0,0,1,1,1,1,1,1,0,0,1,1,0,0,1,1,0,0,0,1,0,1,1,1,0,1,1,0,0,1,0,1,0,0,0,1,1,1,1,0,0,1,1,1,0,1],[1,1,1,1,0,0,1,0,0,1,1,0,1,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1,1,1,0,0,1,1,1,1,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,0],[0,0,0,1,0,0,1,1,1,1,1,1,0,1,0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,0,0,1,1,0,0,0,0,1,0,0,0,1,1,1,1,0,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1],[0,1,0,0,0,0,1,0,1,1,0,0,0,1,0,1,0,1,1,1,0,1,0,0,0,1,1,0,0,0,1,1,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,1,0,1,0,1,0,1,1,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,1,0,0],[1,1,0,0,0,0,0,0,1,0,1,1,1,0,0,1,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,1,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,0,1,0,0,0,0,1,1,0,1,0,1,0,1,0,0,1,0,1,1,1,0,0,1,0,0,1],[1,0,1,0,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,0,1,1,0,0,0,1,0,0,1,0,1,1,1,1,0,0,0,1,0,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1],[1,1,0,0,1,1,0,0,1,0,0,0,1,0,1,1,1,1,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,0,1,0,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,0,0,1,0,1],[0,1,1,1,1,1,1,1,0,1,1,1,0,0,0,0,1,1,0,1,1,1,0,1,1,1,0,0,1,0,1,0,0,1,1,0,0,0,0,1,0,1,1,1,0,1,0,0,0,1,0,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,0,0,1,1,1,0,0,0],[1,0,0,0,0,1,1,0,1,0,1,1,0,0,0,0,1,1,1,1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,1,0,1,1,0,0,1,0,1,1,1,1,0,1,1],[0,0,1,1,1,0,1,0,1,0,0,1,0,1,0,1,1,1,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,1,1,1,1,1,0,0,1,0,1,1,0,0,1,1,1,1,1,1,1,0,1],[1,0,0,1,1,1,1,1,1,1,1,1,0,1,0,0,1,0,1,1,1,0,0,0,0,0,1,1,0,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,0,0,0,1,0,0,1,0,1,1,0,1,0,0,0],[1,0,1,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,1,0,1,0,1,1,0,0,0,0,0,1,1,0,1,0,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1,0,1,1,1,1,0,0,1],[0,1,1,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1,0,1,1,1,1,0,0,1,1,1,0,1,0,1,1,1,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,0,1,0,0,0,0,1,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,0,0,0],[0,0,0,1,0,1,1,0,0,0,1,0,1,0,1,0,1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,0,1,1,0],[0,1,1,0,1,0,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,1,1,0,1,0,0,0,1,0,0,0,1,0,1,1,1,1,0,0,0,1,0,1,1,1,1,0,0,1,1,0,0,1,0,1,1,1,0,1,0,0,0,1,0,1],[0,0,0,0,1,0,1,1,0,1,0,1,1,1,1,0,0,1,1,0,1,0,0,0,1,1,0,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,0,1,0,0,1,0,0,1,1,0,1,1,0,1,0,1,1,0,1,1],[1,1,0,0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,0,1,1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,1,1,0,0,1,0,0,0,1,0,1,1,0,0,0,1,1,0,0,0,1,1,0,1,0,1,1,0,0,1,1,0,0,0,0,1,1,0,0,0,1,0,1,1,1],[1,1,0,1,0,1,0,0,0,0,1,1,0,1,0,0,1,0,0,0,1,0,0,1,1,1,1,1,0,1,0,1,0,0,0,0,1,1,1,1,1,1,0,1,1,0,1,1,1,0,0,0,1,1,1,1,0,1,1,1,0,1,1,0,1,0,0,1,0,0,0,0,0,1,1,1,0,1,0,1],[1,0,0,1,0,0,1,0,0,1,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,1,0,1,1,0,1,0,0,0,1,0,0,1,1,0,0,1,1,0,1,0,1,1,0,1,1,0,1,1,0,1,0,1,1,0],[0,1,1,1,0,1,0,0,0,0,1,0,0,1,1,1,1,0,0,1,0,0,1,0,1,0,1,0,1,1,0,1,1,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,0,1,0,0,1,1,0,0,1,1,0,1,1,1,0,0],[1,0,0,1,0,1,0,1,1,1,0,0,0,1,0,0,1,0,1,1,0,1,1,1,0,0,1,0,0,1,0,0,1,1,0,0,1,0,1,0,1,1,0,1,0,0,0,1,1,0,0,0,0,1,0,1,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,1,1,0,1,1,0,0,0,0],[1,1,0,1,1,1,1,1,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,1,0,1,1,0,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1,0,1,1,0,1,1,1,1,0,1,1,0,1,0,0,1,1,1,1,1,0,1,1,1,1],[1,1,0,0,1,1,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,0,1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,1,1,1,1,1,1,0,0,1,0,1,0,1,1,0,1,1,1,0,0,0,1,1,1,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,0,0,1,1,1,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,1,0,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,0,0,1,1,0,0,0,0,1,0,1,1,1,0,1],[0,1,1,0,0,1,1,1,1,0,1,0,1,0,0,1,0,1,1,1,0,1,1,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,0,1,0,0,1,0,1,0,0,0,0,1,1,1,0,1,1,1,1,0,0,1,1,0,0,0,0,1,0,1,0,1,0,0,1,0,1,1,0,0,0],[0,1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,0,0,0,1,1,0,1,1,0,0,1,1,0,1,1,0,1,0,0,0,1,0,1,1,1,1,1,1,0,0,1,1,1,1,0,1,0,0,1,0,0,1,1,1,0,1,1,1,1,0,0,0,1,1,1,1,1,1,0,1,0,1,0,1],[0,1,1,0,1,1,1,0,1,1,1,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,0,0,1,1,1,0,1,1,1,0,0,1,0,1,0,0],[0,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,0,1,0,1,1,0,0,0,0,0,1,1,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,1,1,0],[0,0,1,0,0,0,0,1,1,1,0,0,1,1,0,1,0,0,0,1,1,1,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,1,1,1,0,0,1,1,0,0,0,1,1,1,0,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0],[0,1,1,1,1,0,1,1,0,1,0,1,1,1,0,0,1,1,1,0,0,0,0,0,1,0,1,0,1,0,1,1,0,0,0,0,0,1,1,0,0,0,1,1,1,1,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1],[1,1,0,0,1,0,1,1,1,0,1,1,0,0,0,0,0,1,1,1,0,1,0,0,1,0,1,0,0,1,0,1,1,1,1,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,1,0,1,1,0,0,1,0,1,1,1,0,0,0,0,0,1,0],[1,1,1,0,0,1,0,1,1,0,0,1,0,1,1,1,0,0,0,1,0,0,1,1,0,0,0,1,1,0,1,1,1,0,0,1,0,0,1,0,1,0,0,0,1,1,1,1,1,0,0,1,0,1,0,1,0,0,0,0,0,1,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,1,0,0],[1,0,1,1,1,0,1,1,1,0,0,0,0,0,1,0,0,1,0,1,0,1,0,1,0,0,1,1,0,0,0,1,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,0,0,1,1,1,1,0,1,0,0,0,0,1,0,1,1,0,0,0,1,0,1,1,0,1,1,1,1,1,1,0],[1,1,1,0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,0,1,0,0,1,1,1,0,0,1,0,1,0,1,1,0,1,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,0,1,1,0,0,1,1,0,1,0,1,0,1,1,0,1,1,1,0],[0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,0,1,1,1,1,0,0,1,0,1,1,1,0,1,1,0,0,1,1,1,1,0,0,1,0,0,1,1,1,0,0,0,1,0,0,1,1,1,0,0,0,1,1,0,0,1,0,0,1,0,1,0,0,0,1,1,1,1,0,0,1,0,1,0,1],[0,1,1,0,1,1,0,1,1,0,1,1,1,0,0,0,0,0,1,0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,1,0,0,1,1,1,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0,0,0,1,0,1,0,1,0,0,0,0,1,0,1,0,0,1,0],[1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,0,1,1,0,1,0,0,0,1,0,0,1,1,1,1,0,0,1,1,1,1,0,1,1,0,0,0,1,1,1,0,1,1,1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,0,0,1,0,1,1,1,1,0,0,0,1,1,1,1],[0,1,0,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,1,0,1,0,0,1,1,0,1,1,1,0,0,1,0,1,1,0,1,0,1,0,0,1,0,0,0,1,0,0,1,1,0,0,1,1,1,1,1,0,1,1,0,0,0,1,0,1,1,1,1,1,0,0,1,0,1,0,1,0,0,1],[0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,1,1,0,0,1,1,1,1,0,1,1,0,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,0,1],[0,0,1,0,1,1,0,1,1,1,1,1,0,1,0,1,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,1,0,1,0,0,1,0,1,1,0,1,1,1,0,1,0,0,1,0,0,1,0,1,0,1,1,0,1,0,0,0],[1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,1,1,1,0,1,1,1,1,0,0,1,1,0,1,1,0,0,1,1,1,1,1,0,1,0,0,0,1,1,1,0,1,1,1,1,0,1,1,0,0,1,1,0,0,0,0,1,0,0,1,1,0,1,0,0,1],[1,1,0,0,0,1,0,0,1,1,0,0,1,1,0,1,0,1,0,1,1,1,0,0,1,0,0,0,0,0,0,1,0,1,1,0,1,0,1,0,0,1,0,1,1,1,1,0,0,1,1,0,1,1,0,1,1,0,0,1,0,0,0,1,0,0,0,0,1,1,1,0,1,0,0,0,1,1,1,0],[0,0,0,1,0,1,0,1,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,0,0,0,1,0,0,1,1,0,0,0,1,0,1,1,0,1,0,1,1,1,1,0,1,1,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0],[0,0,1,1,1,0,1,0,0,1,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,1,0,1,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0,1,0,0,1,1,1,1,0,1,1,0,0,0,1,1,0,1,1,1],[1,1,1,1,0,0,0,1,1,1,0,1,0,0,0,0,0,0,1,1,1,0,1,1,1,0,1,1,0,0,0,1,0,1,1,0,1,1,0,1,1,1,0,1,1,0,1,1,0,0,1,0,1,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,1,1,1],[0,1,1,0,1,1,0,1,0,1,1,1,0,1,0,1,1,0,0,0,0,1,0,1,0,0,1,1,1,1,1,0,0,1,1,0,1,1,0,0,0,0,0,1,0,1,1,0,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0],[1,1,0,0,1,1,0,1,0,1,0,1,0,0,1,1,0,1,0,0,1,1,0,1,1,0,1,0,1,1,1,0,0,1,0,0,0,1,1,0,1,0,0,0,0,1,0,1,0,1,1,1,1,1,1,1,1,0,1,0,0,0,0,1,1,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0],[1,0,1,1,1,0,1,1,0,1,1,0,1,0,0,1,0,0,1,1,0,1,1,1,0,0,0,1,0,0,1,0,1,0,1,1,1,0,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0,0,0,0,0,1,1,0,1],[0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,1,0,1,0,0,1,1,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,1,1,1,1,0,1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,0,0,1,0,1,0,1,1,1,1,1],[0,1,0,1,1,0,1,1,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,1,1,1,0,0,1,0,0,0,0,0,1,1,1,1,0,1,1,0,1,0,1,0,0,1,0,1,1,1,0,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,1,0,1,0,0,1,1,0,0],[0,1,1,1,0,1,1,0,1,1,1,0,0,1,1,0,1,1,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,0,0,1,1,0,0,0,0,1],[1,0,0,0,0,0,1,1,0,1,1,1,1,1,1,1,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,0,1,1,0,0,1,1,1,0,1,1,1,0,0,0,1,1,0,0,0,0,1,1,1,0,0,0,1,0,0,1,1,1,1,0,1,0,1,0,0,0,1],[1,0,0,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1,0,1,1,0,0,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,0,1,0,1,0,1,0,0,1,1,1,1,0,1,1,0,0,0,1,0,0,1,0,1,1,0,0,0,1,1,1],[0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,1,1,1,0,0,0,0,1,1,0,1,1,0,1,0,1,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,1,0,1],[0,0,0,0,1,0,0,0,1,0,0,1,1,0,1,0,1,1,1,0,1,0,0,1,1,0,0,0,1,0,0,0,0,0,0,1,1,1,0,1,1,0,0,1,1,0,0,0,1,0,1,0,1,1,1,0,0,0,1,1,1,0,1,1,1,1,0,0,0,0,1,1,0,1,1,0,0,0,1,1],[1,0,1,1,1,0,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,1,0,0,1,1,1,0,0,0,0,0,1,1,1,0,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,1,1,0,0,1,0,1,1,1,1,0],[1,0,0,1,0,1,0,1,0,0,0,0,0,1,0,1,1,1,0,0,1,0,1,1,1,1,1,0,1,0,1,0,0,1,1,1,1,0,1,1,1,0,0,0,0,0,1,0,1,1,1,1,0,1,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,1,1,1,1,0,1,1,1,1,1,1],[1,0,0,0,0,1,1,0,1,0,0,0,0,0,1,1,0,1,0,1,0,0,1,0,1,1,0,0,0,0,1,1,0,1,0,0,1,0,1,0,1,0,0,1,1,1,0,1,0,0,0,1,1,0,1,1,1,1,1,1,0,0,1,0,1,0,1,0,0,1,1,1,1,1,0,1,0,1,0,1]]
print(Solution().maxDistance(input2))