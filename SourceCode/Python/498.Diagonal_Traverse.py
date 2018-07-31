'''

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]

Explanation:
https://leetcode.com/static/images/problemset/diagonal_traverse.png

Note:
The total number of elements of the given matrix will not exceed 10,000.


'''


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        k = 1
        kFlag = False
        a = [-1, 1]
        ans = []
        row = len(matrix)
        col = len(matrix[0])
        i = 0
        j = 0
        while True:
            ans.append(matrix[i][j])
            if i == row-1 and j == col-1:
                break
            print ans
            i, j = i+k*a[0], j+k*a[1]
            if i > row-1:
                j += 2
                i = row-1

                kFlag = True
            if j > col-1:
                i += 2
                j = col-1
                kFlag = True
            if i < 0:
                i = 0
                kFlag = True
            if j < 0:
                j = 0
                kFlag = True


            if kFlag == True:
                k = -k
                kFlag = False
        return ans




board = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

board2 = [[3],[2]]
print Solution().findDiagonalOrder(board)