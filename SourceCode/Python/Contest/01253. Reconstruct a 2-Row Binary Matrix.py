'''

5256->1253. Reconstruct a 2-Row Binary Matrix
Difficulty: Medium
Given the following details of a matrix with n columns and 2 rows :

The matrix is a binary matrix, which means each element in the matrix can be 0 or 1.
The sum of elements of the 0-th(upper) row is given as upper.
The sum of elements of the 1-st(lower) row is given as lower.
The sum of elements in the i-th column(0-indexed) is colsum[i], where colsum is given as an integer array with length n.
Your task is to reconstruct the matrix with upper, lower and colsum.

Return it as a 2-D integer array.

If there are more than one valid solution, any of them will be accepted.

If no valid solution exists, return an empty 2-D array.



Example 1:

Input: upper = 2, lower = 1, colsum = [1,1,1]
Output: [[1,1,0],[0,0,1]]
Explanation: [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.
Example 2:

Input: upper = 2, lower = 3, colsum = [2,2,1,1]
Output: []
Example 3:

Input: upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
Output: [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]


Constraints:

1 <= colsum.length <= 10^5
0 <= upper, lower <= colsum.length
0 <= colsum[i] <= 2



'''


class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        s2_cnt = colsum.count(2)
        if upper + lower != sum(colsum) or upper < s2_cnt or lower < s2_cnt:
            return []

        upper -= s2_cnt
        lower -= s2_cnt
        ans = [[],[]]
        for s in colsum:
            if s == 2:
                ans[0].append(1)
                ans[1].append(1)
            elif s == 1:
                if upper > 0:
                    upper -= 1
                    ans[0].append(1)
                    ans[1].append(0)
                else:
                    lower -= 1
                    ans[0].append(0)
                    ans[1].append(1)
            elif s == 0:
                ans[0].append(0)
                ans[1].append(0)

        return ans
