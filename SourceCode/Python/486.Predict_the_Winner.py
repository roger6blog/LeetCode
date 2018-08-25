'''

Given an array of scores that are non-negative integers.

Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on.

Each time a player picks a number,

that number will not be available for the next player.

This continues until all the scores have been chosen.

The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner.

You can assume each player plays to maximize his score.

Example 1:
Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2.
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5,
then player 1 will be left with 1 (or 2).
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
Hence, player 1 will never be the winner and you need to return False.

Example 2:
Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7.
No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12),
so you need to return True representing player1 can win.
Note:
1 <= length of the array <= 20.
Any scores in the given array are non-negative integers and will not exceed 10,000,000.
If the scores of both players are equal, then player 1 is still the winner.


'''


class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        length = len(nums)

        if length % 2 == 0 or length == 1:
            return True

        dp = [[0 for _ in xrange(length)] for _ in xrange(length)]
        for x in xrange(length):
            dp[x][x] = nums[x]

        sum = [0] * length
        sum[0] = nums[0]
        for i in xrange(length-1):
            sum[i+1] = sum[i] + nums[i+1]

        for i in xrange(1, length):
            for j in xrange(0, length - i):
                dp[j][i+j] = max(sum[i+j] - sum[j] + nums[j] - dp[j+1][i+j],
                                 sum[i+j] - sum[j] + nums[j] - dp[j][i+j-1]
                                 )

        return 2 * dp[0][length-1]  >= sum[length-1]


    def PredictTheWinnerTLE(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        length = len(nums)
        return self.findAns(nums, 0, length-1) >=0

    def findAns(self, nums, i, j):
        if  i == j:
            return nums[i]
        else:
            first = nums[i] - self.findAns(nums, i+1, j)
            last = nums[j] - self.findAns(nums, i, j-1)
            return max(first, last)


Input= [1, 5, 2]
LongInput = [1398871,3911315,3298661,725450,9541448,915835,3155005,58239,1541250,6094565,7622099,1953520,5565179,5923565,1842903,7679819,7288290,8409862,1747401,1662260]
print Solution().PredictTheWinnerTLE(LongInput)