'''

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x,

and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n >= 1, find out how much money you need to have to guarantee a win.

Credits:
Special thanks to @agave and @StefanPochmann for adding this problem and creating all test cases.


'''

import sys
import datetime
class Solution(object):
    def getMoneyAmountRec(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = []
        for _ in xrange(n+1):
            dp.append([0] * (n+1))
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        left = 1
        right = n
        ans = self.solve(dp, left, right)
        return ans


    def solve(self, dp, left, right):
        if left >= right:
            return 0

        if dp[left][right]:
            return dp[left][right]

        # dp[left][right] = min(i + max(self.solve(dp, left, i - 1), self.solve(dp, i + 1, right)) for i in range(left, right + 1))



        minCost = sys.maxint
        for guess in xrange(left, right+1):
            # print("guess: {}".format(guess))
            smaller = self.solve(dp, left, guess - 1)
            higher = self.solve(dp, guess + 1, right)
            minCost = min(minCost, max(smaller , higher) + guess)
        # print("minCost: of guess number {}: {}".format(guess, minCost))
        dp[left][right] = minCost


        return dp[left][right]

    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = []
        for _ in xrange(n + 1):
            dp.append([0] * (n + 1))
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for left in xrange(n-1, -1, -1):
            for right in xrange(left+1, n+1):
                dp[left][right] = sys.maxint
                for guess in xrange(left, right, 1):
                    dp[left][right] = min(dp[left][right], guess + max(dp[left][guess-1], dp[guess+1][right]))
        return dp[1][n]

    def BinarySearch(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        guess = 8
        amount = 0

        while left < right:
            mid = (left + right) / 2

            amount += mid
            print("Amount: {}".format(amount))
            if mid > guess:
                right = mid - 1
            elif mid < guess:
                left = mid + 1
            else:
                return amount



start = datetime.datetime.now()
print Solution().getMoneyAmount(5)
end = datetime.datetime.now()
print end - start