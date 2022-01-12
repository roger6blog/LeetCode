'''
Level: Medium

We are playing the Guessing Game. The game will work as follows:

I pick a number between 1 and n.
You guess a number.
If you guess the right number, you win the game.
If you guess the wrong number, then I will tell you whether the number I picked is higher or lower, and you will continue guessing.
Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.
Given a particular n, return the minimum amount of money you need to guarantee a win regardless of what number I pick.


Example 1:


"../../../Material/graph.png"

Input: n = 10
Output: 16
Explanation: The winning strategy is as follows:
- The range is [1,10]. Guess 7.
    - If this is my number, your total is $0. Otherwise, you pay $7.
    - If my number is higher, the range is [8,10]. Guess 9.
        - If this is my number, your total is $7. Otherwise, you pay $9.
        - If my number is higher, it must be 10. Guess 10. Your total is $7 + $9 = $16.
        - If my number is lower, it must be 8. Guess 8. Your total is $7 + $9 = $16.
    - If my number is lower, the range is [1,6]. Guess 3.
        - If this is my number, your total is $7. Otherwise, you pay $3.
        - If my number is higher, the range is [4,6]. Guess 5.
            - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $5.
            - If my number is higher, it must be 6. Guess 6. Your total is $7 + $3 + $5 = $15.
            - If my number is lower, it must be 4. Guess 4. Your total is $7 + $3 + $5 = $15.
        - If my number is lower, the range is [1,2]. Guess 1.
            - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $1.
            - If my number is higher, it must be 2. Guess 2. Your total is $7 + $3 + $1 = $11.
The worst case in all these scenarios is that you pay $16. Hence, you only need $16 to guarantee a win.

Example 2:

Input: n = 1
Output: 0
Explanation: There is only one possible number, so you can guess 1 and not have to pay anything.
Example 3:

Input: n = 2
Output: 1
Explanation: There are two possible numbers, 1 and 2.
- Guess 1.
    - If this is my number, your total is $0. Otherwise, you pay $1.
    - If my number is higher, it must be 2. Guess 2. Your total is $1.
The worst case is that you pay $1.


Constraints:

1 <= n <= 200


==================== Old Descriptions =======================


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

Hint:

The best strategy to play the game is to minimize the maximum loss you could possibly face. Another strategy is to minimize the expected loss.
Here, we are interested in the first scenario.
Take a small example (n = 3). What do you end up paying in the worst case?
Check out this article if you're still stuck.
The purely recursive implementation of minimax would be worthless for even a small n. You MUST use dynamic programming.
As a follow-up, how would you modify your code to solve the problem of minimizing the expected loss, instead of the worst-case loss?

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