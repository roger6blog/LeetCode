'''

5073->1197. Minimum Knight Moves
Difficulty: Medium
In an infinite chess board with coordinates from -infinity to +infinity,

you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below.

Each move is two squares in a cardinal direction, then one square in an orthogonal direction.



Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.



Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]


Constraints:

|x| + |y| <= 300


'''
import math
class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        x = abs(x)
        y = abs(y)
        if y > x:
            y, x = x, y

        if x == 2 and y == 2:
            return 4
        if x == 1 and y == 0:
            return 3



        if y>x-y:
            return int(x-y - 2*math.floor((x-2*y)/3))

        else:
            return int(x-y - 2*math.floor((x-2*y)/4))



x = 1
y = 2
print(Solution().minKnightMoves(x, y))