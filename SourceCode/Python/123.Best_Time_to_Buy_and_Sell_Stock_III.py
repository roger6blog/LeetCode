'''

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.

You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time

(i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        buy1 = -prices[0]
        buy2 = -prices[0]
        sell1 = 0
        sell2 = 0

        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)
        return sell2


    def maxProfitDP(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        length = len(prices)
        dp1 = [0] * length
        dp2 = [0] * length

        ans = 0

        # dp1: the max revenue of trade before price[x]
        minPrice = prices[0]
        for x in xrange(1, length):
            minPrice = min(minPrice, prices[x])
            dp1[x] = max(dp1[x-1], prices[x] - minPrice)

        # dp2: the max revenue of trade after price[x]
        maxPrice = prices[-1]
        for x in xrange(length-1, -1, -1):
            maxPrice = max(maxPrice, prices[x])
            dp2[x] = max(dp2[x], maxPrice - prices[x])

        for x in xrange(len(dp1)):
            ans = max(ans, dp1[x] + dp2[x])

        return ans

stock = [3,3,5,0,0,3,1,4]
print Solution().maxProfit(stock)