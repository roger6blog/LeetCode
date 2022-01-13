'''
Level: Medium Tag: DP

You are given an integer array coins representing coins of different denominations

and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.

If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.


Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0


Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104


'''


'''
要用指定數量的硬幣湊到規定的數字
我們用DP[a]來表示湊到a數字所需要的硬幣個數,
如果今天a = 10, 有三種硬幣1, 2, 5
那dp[10]可以是10個1, 5個2, 2個5
以最少目標來說 dp[10]就可以是dp[10-5]+1種湊數方式
所以狀態轉移方程式為min(dp[a], dp[a-c]+1)

'''


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins or len(coins) == 0 or amount < 0:
            return -1
        if min(coins) > amount:
            return -1

        if amount == 0:
            return 0
        from sys import maxint
        dp = [maxint for i in range(amount+1)]
        dp[0] = 0
        for c in coins:
            if c < amount:
                dp[c] = 1

        for a in range(1, amount+1):
            for c in coins:
                change = a - c
                if change < 0 or dp[change] == maxint:
                    continue

                dp[a] = min(dp[a], dp[change]+1)


        if dp[amount] == maxint:
            dp[amount] = -1
        print(dp[amount])
        return dp[amount]


coins = [1,2,5]
amount = 11
assert 3 == Solution().coinChange(coins, amount)

coins = [0]
amount = 1
assert -1 == Solution().coinChange(coins, amount)

coins = [1]
amount = 0
assert -1 == Solution().coinChange(coins, amount)

coins = [2]
amount = 1
assert -1 == Solution().coinChange(coins, amount)


coins = [1,2147483647]
amount = 2
assert 2 == Solution().coinChange(coins, amount)