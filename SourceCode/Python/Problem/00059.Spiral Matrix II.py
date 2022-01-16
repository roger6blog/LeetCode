'''
Level: Medium  Tag: Matrix

Given a positive integer n,

generate an n x n matrix filled with elements from 1 to n^2 in spiral order.



Example 1:

"../../../Material/spiraln.jpg"

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:

Input: n = 1
Output: [[1]]


Constraints:

1 <= n <= 20

'''


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        matrix = [[0 for _ in range(n)] for _ in range(n)]

        RIGHT = 0
        DOWN = 1
        LEFT = 2
        UP = 3

        right = n-1
        down = n-1
        left = 0
        up = 0

        dx = []
        direction = 0

        for i in range(1, n*n+1)[::-1]:
            dx.append(i)

        while left <= right and up <= down:
            if direction == RIGHT:
                for i in range(left, right+1):
                    matrix[up][i] = dx.pop()
                up += 1
            elif direction == DOWN:
                for i in range(up, down+1):
                    matrix[i][right] = dx.pop()
                right -= 1
            elif direction == LEFT:
                for i in range(right, left-1, -1):
                    matrix[down][i] = dx.pop()
                down -= 1
            elif direction == UP:
                for i in range(down, up-1, -1):
                    matrix[i][left] = dx.pop()
                left += 1
            direction = (direction +1) % 4

        print(matrix)
        return matrix

n = 3
Solution().generateMatrix(n)