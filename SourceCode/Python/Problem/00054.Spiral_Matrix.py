'''
Level: Medium   Tag: Matrix
Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order.

Example 1:

"../../../Material/spiral1.jpg"

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

"../../../Material/spiral.jpg"

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        RIGHT = 0
        DOWN = 1
        LEFT = 2
        UP = 3
        if matrix == []:
            return []
        ans = []
        direction = RIGHT
        upRow = 0
        leftCol = 0
        downRow = len(matrix) - 1
        rightCol = len(matrix[0]) - 1

        while upRow <= downRow and leftCol <= rightCol:
            if direction == RIGHT:
                for i in xrange(leftCol, rightCol+1):
                    ans.append(matrix[upRow][i])
                # finish one upRow
                upRow += 1
            elif direction == DOWN:
                for i in xrange(upRow, downRow+1):
                    ans.append(matrix[i][rightCol])
                # finish one rightCol
                rightCol -= 1
            elif direction == LEFT:
                for i in xrange(rightCol, leftCol-1, -1):
                #for i in range(leftCol, rightCol + 1)[::-1]:
                    ans.append(matrix[downRow][i])
                # finish one downRow
                downRow -= 1
            else:
                for i in xrange(downRow, upRow-1, -1):
                #for i in range(upRow, downRow + 1)[::-1]:
                    ans.append(matrix[i][leftCol])
                # finish one leftCol
                leftCol += 1
            direction = (direction + 1 ) % 4
        return ans



    def spiralOrder2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        RIGHT = 0
        DOWN = 1
        LEFT = 2
        UP = 3

        m = len(matrix)
        n = len(matrix[0])
        right = n-1
        down = m-1
        left = 0
        up = 0
        direction = 0
        ans = []
        while right >= left and up <= down:
            if direction == RIGHT:
                for i in range(left, right+1):
                    ans.append(matrix[up][i])
                up += 1
            elif direction == DOWN:
                for i in range(up, down+1):
                    ans.append(matrix[i][right])
                right -= 1
            elif direction == LEFT:
                # 因為有負數 不能用range..[::-1] 會出錯
                for i in range(right, left-1, -1):
                    ans.append(matrix[down][i])
                down -= 1
            elif direction == UP:
                # 因為有負數 不能用range..[::-1] 會出錯
                for i in range(down, up-1, -1):
                    ans.append(matrix[i][left])
                left += 1

            direction = (direction + 1) % 4

        print(ans)

        return ans




q = [
[ 1, 2, 3 ],
[ 4, 5, 6 ],
[ 7, 8, 9 ]
]
q2 = [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
ans = sol.spiralOrder(q2)
print(sol.spiralOrder2(q2))


