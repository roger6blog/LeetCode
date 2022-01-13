'''
Level: Medium Tag: DP

There are a row of n houses,

each house can be painted with one of the three colors: red, blue or green.

The cost of painting each house with a certain color is different.

You have to paint all the houses such that no two adjacent houses have the same color,

and you need to cost the least. Return the minimum cost.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix.

For example, costs[0][0] is the cost of painting house 0 with color red;
costs[1][2] is the cost of painting house 1 with color green, and so on...

Find the minimum cost to paint all houses.

All costs are positive integers.


Example 1:

Input: [[14,2,11],[11,14,5],[14,3,10]]
Output: 10
Explanation: Paint house 0 into blue,
             paint house 1 into green,
             paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.

Example 2:

Input: [[1,2,3],[1,4,6]]
Output: 3

'''

'''

設DP[i][j]為漆到第i個房子 塗上j顏色時的總花費，所以j只能為0~2
則漆到第i間房子的最低花費就是 DP[i][j] = DP[i-1][k] + cost[i][j]  cost為第i間房子塗上j顏色所需的費用
所以k顏色必須不等於j顏色


'''



class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        n = len(costs)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

        # 初始值，第一間房子塗上指定顏色的cost
        for i in range(3):
            dp[0][i] = costs[0][i]

        for i in range(1, n):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

        ans = min(dp[n-1][0], dp[n-1][1], dp[n-1][2])
        print(ans)
        return ans



costs = [[14,2,11],[11,14,5],[14,3,10]]
assert 10 == Solution().minCost(costs)

costs = [[1,2,3],[1,4,6]]
assert 3 == Solution().minCost(costs)