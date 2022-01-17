'''
Level: Medium    Tag: Matrix

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

Example 2:

Input: matrix = [[-5]], k = 1
Output: -5


Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-10^9 <= matrix[i][j] <= 10^9
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2

Note:
You may assume k is always valid, 1 <= k <= n^2.

Follow up:

Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.

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




    def kthSmallest2(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def smaller_count(matrix, num):
            row = len(matrix)
            col = len(matrix[0])
            count = 0

            for i in range(row):
                for j in range(col):
                    if matrix[i][j] <= num:
                        count += 1

            return count


        left = matrix[0][0]
        right = matrix[-1][-1]


        while left+1 < right:  # 不加1逼近不了
            mid = left + (right-left) // 2
            if smaller_count(matrix, mid) < k:
                left = mid
            else:
                right = mid


        if smaller_count(matrix, left) >= k:
            return left
        else:
            return right



matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8

print(Solution().kthSmallest2(matrix, k))