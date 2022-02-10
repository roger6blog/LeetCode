'''
Level: Medium

You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of a rectangle formed from these points,

with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.



Example 1:

"../../../Material/rec1.jpeg"

Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4

Example 2:

"../../../Material/rec2.jpeg"

Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2


Constraints:

1 <= points.length <= 500
points[i].length == 2
0 <= xi, yi <= 4 * 10^4
All the given points are unique.
'''

class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
