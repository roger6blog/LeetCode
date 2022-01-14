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





    '''
    設DP[n][m] 為塗第n根柱子時 前一個柱子是否與其同色 m只能是0或1，0為不同色 1為同色
    如果DP[n][1]時，代表前一個柱子n-1和第n根柱子同色
    此時的DP[n-1]的方法數就是有以下兩種 :
            1. DP[n-1][0] * (k-1)  和前一根柱子不同色，有k-1種顏色可選

            2. DP[n-1][1] * (k-1)  如果你非要跟前一根柱子同色，那你就還是只能選k-1種顏色
                                   因為第i-2根柱子用的顏色和第i-1根用的顏色一樣，
                                   所以我們不能用第i-2根柵欄用的顏色相同的顏色，不然就會三根柱子同色了

    如果DP[n][0]時，代表前一個柱子n-1和第n根柱子不同色
    此時的DP[n][0]就直接是DP[n-1][1]的方法數
    最後答案就是選擇同色和選擇不同色的方法數的加總

    '''



    def numWays3(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        dp = [[0] * 2 for _ in range(n+1)]
        # 初始值設定
        # 第1根沒有前面的人跟你同色，所以有k種方法
        dp[1][1] = k

        for i in range(2, n+1):
            dp[i][0] = dp[i-1][1]
            dp[i][1] = (dp[i-1][0] + dp[i-1][1]) * (k-1)

        ans = dp[i][0] + dp[i][1]
        print(ans)

        return ans

n=7
k=3
print(Solution().numWays(n, k))
print(Solution().numWays2(n, k))
assert 1344 == Solution().numWays3(n, k)
n=3
k=2
assert 6 == Solution().numWays3(n, k)