'''

Given a n x n matrix where each of the rows and columns are sorted in ascending order,

find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order,

not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 <= k <= n^2.


'''


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0])
        ans = []
        for i in xrange(row):
            for j in xrange(col):
                ans.append(matrix[i][j])
        ans.sort()
        return ans[k-1]

    def kthSmallest_BinSearch(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        left = matrix[0][0]
        right = matrix[-1][-1]

        while left < right:
            temp = 0
            mid = (left + right) / 2
            for row in matrix:
                temp += self.binarySearchK(row, mid)
            if temp < k:
                left = mid + 1
            else:
                right = mid
        return right

    def binarySearchK(self, row, x):
        length = len(row)
        left = 0
        right = length
        while left < right:
            mid = (left + right) / 2
            if row[mid] <= x:
                left = mid + 1
            else:
                right = mid
        return left

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8

print Solution().kthSmallest_BinSearch(matrix, k)