'''
Level: Medium  Tag: 2DP

There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.

Example 1:

Input: n=3, k=2
Output: 6
Explanation:
          post 1,   post 2, post 3
    way1    0         0       1
    way2    0         1       0
    way3    0         1       1
    way4    1         0       0
    way5    1         0       1
    way6    1         1       0

Example 2:

Input: n=2, k=2
Output: 4
Explanation:
          post 1,   post 2
    way1    0         0
    way2    0         1
    way3    1         0
    way4    1         1


'''






'''
設DP[i][j][k]為第i根柵欄弄成j色，前面有k個一樣顏色的方法數
根據提議不能超過2個同色的柵欄相同顏色，所以k只會是1個顏色或2個顏色相同 即k=1 or k=2
則DP[i][j][k]有幾種狀況:
前面有2種顏色相同時，DP為DP[i][j][1]
兩個相鄰顏色代表我不能再繼續塗同一顏色了
所以DP[i][j][1] = DP[i-1][]

所以應該是DP[m][k] = DP[m-1][x] * (k-1) + DP[m-2][x] * (k-1)





'''




class Solution(object):
    def numWays2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0: return 0
        if n == 1: return k

        # for the first 2 posts
        sameColor = k
        diffColor = k * (k - 1)

        for i in range(2, n):
            temp = diffColor
            diffColor = (sameColor + diffColor) * (k - 1)
            sameColor = temp

        return sameColor + diffColor

    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        diff = [0]*(n+1)
        diff[1] = k
        diff[2] = k*(k-1)

        for i in xrange(3, n+1):
            diff[i] = (diff[i-1] + diff[i-2]) * (k-1)
        same = diff[n - 1]
        return diff[n] + same






    def numWays3(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """



n=7
k=3
print(Solution().numWays(n, k))
print(Solution().numWays2(n, k))
print(Solution().numWays3(n, k))