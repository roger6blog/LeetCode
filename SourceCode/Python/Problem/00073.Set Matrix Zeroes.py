'''
Level: Medium   Tag: Matrix

Given an m x n integer matrix matrix,

if an element is 0, set its entire row and column to 0's,

and return the matrix.

You must do it in place.

Example 1:

"../../../Material/73-mat1.jpg"

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

"../../../Material/73-mat2.jpg"

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1


Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?


'''


'''
暴力作法 開一個同樣大小mxn的矩陣，然後掃描原矩陣 只要有某一行有0 就把新矩陣對應的該行列都設0
set作法 先掃描一次矩陣行列，看到有0的就把他的行列編號記下來
        再重掃一次矩陣，有看到對應編號在set裡的就設為0
'''


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        if not matrix:
            return matrix

        col = len(matrix)
        row = len(matrix[0])
        col_zero = set()
        row_zero = set()


        for i in range(col):
            for j in range(row):
                if matrix[i][j] == 0:
                    col_zero.add(i)
                    row_zero.add(j)

        for i in range(col):
            for j in range(row):
                if i in col_zero or j in row_zero:
                    matrix[i][j] = 0


        print(matrix)

        return matrix




matrix = [[1,1,1],[1,0,1],[1,1,1]]
Solution().setZeroes(matrix)