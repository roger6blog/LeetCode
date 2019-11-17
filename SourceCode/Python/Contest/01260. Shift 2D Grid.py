'''

5263->1260. Shift 2D Grid
Difficulty: Easy
Given a 2D grid of size n * m and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] becomes at grid[i][j + 1].
Element at grid[i][m - 1] becomes at grid[i + 1][0].
Element at grid[n - 1][m - 1] becomes at grid[0][0].
Return the 2D grid after applying shift operation k times.



Example 1:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
Example 2:


Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
Example 3:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]


Constraints:

1 <= grid.length <= 50
1 <= grid[i].length <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100



'''
import copy
class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        for x in range(k):
            ans = []
            for i in range(len(grid)):
                ans.append([])
            for i in range(len(grid)):
                ans[i].extend([0]*len(grid[0]))
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    #print(grid[i][j])
                    if j == len(grid[i])-1 and i != len(grid)-1:
                        ans[i+1][0] = grid[i][j]
                    elif j == len(grid[i])-1 and i == len(grid)-1:
                        ans[0][0] = grid[i][j]
                    else:
                        ans[i][j+1] = grid[i][j]
            grid = ans
        return grid



grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 4
print(Solution().shiftGrid(grid, 4))