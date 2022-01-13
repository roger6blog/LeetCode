'''
Level: Mdeium  Tag: DP

Given an m x n binary matrix filled with 0's and 1's,

find the largest square containing only 1's and return its area.


Example 1:

"../../../Material/max1grid.jpeg"

Input: matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]
Output: 4

Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.


'''





'''

假設DP[m][n]為長度m x n時所有元素全部都是1的matrix的邊長
那麼DP[m][n]為可以拓展正方形的點，因為這個點是矩陣的右下角
所以左上角的點DP[m-1][n-1], DP[m][n-1], DP[m-1][n]的最小值 只要再加1就是DP[m][n]
所以狀態轉移方程式為 DP[m][n] = min(DP[m-1][n-1], DP[m][n-1], DP[m-1][n]) + 1
邊界情況如果m,n 都是0, 此時必定無法拓展正方形，所以初始值為0

'''


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n == 0:
            return 0

        dp = [[0 for _ in range(n)] for _ in range(m)]


        #初始化
        for i in range(m):
            dp[i][0] = int(matrix[i][0])

        for j in range(n):
            dp[0][j] = int(matrix[0][j])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                else:
                    dp[i][j] = 0


        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dp[i][j])

        print(ans ** 2)

        return ans ** 2


matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]
Solution().maximalSquare(matrix)