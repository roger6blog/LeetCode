'''
Level: Medium      Tag: Matrix

Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Example 1:

Consider the following matrix:

"../../../Material/searchgrid2.jpg"

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.



Example 2:

"../../../Material/searchgrid.jpg"


Given target = 20, return false.

Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matrix[i][j] <= 109
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-109 <= target <= 109

'''

'''
這矩陣不是一般的遞增矩陣
是左下角比右上角大的遞增矩陣，不能用二分法搜尋
這矩陣的特色是越往左數字越小 往右數字越大
所以單純的選一個數字來比較 (例如挑右上角的數字)
如果比目標數大就往左，比目標數小就往下
直到找到或超出邊界為止
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

        row = len(matrix)
        col = len(matrix[0])

        if row == 0 or col == 0:
            return False

        i = 0
        j = col - 1

        while i < row and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False






matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

print(Solution().searchMatrix(matrix, 5))


matrix = [[1,4],[2,5]]
target = 4
print(Solution().searchMatrix(matrix, 4))