'''
Level: Medium Tags:[DP]
Say you have an array for which the i(th) element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.

You may complete as many transactions as you like

(ie, buy one and sell one share of the stock multiple times)

with the following restrictions:

You may not engage in multiple transactions at the same time

(ie, you must sell the stock before you buy again).

After you sell your stock,

you cannot buy stock on next day. (ie, cooldown 1 day)

Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]


'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        length = len(prices)
        buy = [0] * length
        sell = [0] * length
        sell[0] = 0
        buy[0] = -prices[0]
        for i in xrange(1, length):
            if i < 2:
                buy[i] = max(-prices[i], buy[i-1])
            else:
                buy[i] = max(sell[i-2]-prices[i], buy[i-1])
            sell[i] = max(buy[i-1]+prices[i], sell[i-1])
        return sell[length-1]


class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''
        There are 4 actions we can do at one day:
        1. has 0 stock, and buy it
        2. has 1 stock, but do nothing
        3. has 0 stock, then do nothing
        4. has 1 stock, then sell it

        If you choose action 1 at i day, what action you can do is 3 at i-1 day
        If you choose action 2 at i day, what action you can do is 1 or 2 at i-1 day
        If you choose action 3 at i day, what action you can do is 2 or 3 at i-1 day
        If you choose action 4 at i day, what action you can do is 1 or 4 at i-1 day
        '''


        if len(prices) < 2:
            return 0

        has0_buy_1 = -prices[0]
        has1_do_nothing = -prices[0]
        has0_do_nothing = 0
        has1_sell_1 = 0



        for i in range(len(prices)):
            has0_buy_1 = -prices[i] + has0_do_nothing
            has1_do_nothing = max(has1_do_nothing, has0_buy_1)
            has0_do_nothing = max(has1_sell_1, has0_do_nothing)
            has1_sell_1 = prices[i] + has1_do_nothing

        return max(has1_sell_1, has0_do_nothing)





stock = [1,2,3,0,2]
print(Solution().maxProfit(stock))
stock = [1,2,3,0,2]
print(Solution2().maxProfit(stock))