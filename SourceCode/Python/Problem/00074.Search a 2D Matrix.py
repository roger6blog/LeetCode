'''
Level: Medium      Tag: [Matrix], [Binary Search]

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

"../../../Material/mat.jpg"

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20]
  [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:

"../../../Material/74-mat2.jpg"

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        for x in xrange(len(matrix)):
            if target in matrix[x]:
                return True

        return False

    def BinsearchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row * col
        while left < right:
            mid = left + (right - left) / 2
            if matrix[mid / col][mid % col] >= target:
                right = mid
            else:
                left = mid + 1

        return left < row * col and matrix[left / col][left % col] == target




    def BinsearchMatrix2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False


        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row * col

        while left < right:
            mid = left + (right-left) // 2
            val = matrix[mid // col][mid % col]
            if val == target:
                return True
            elif val > target:
                right = mid
            else:
                left = mid + 1

        return False






matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

print(Solution().BinsearchMatrix(matrix, 3))