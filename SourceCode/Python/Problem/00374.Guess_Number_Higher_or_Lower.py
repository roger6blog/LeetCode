'''
Level: Easy

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!

Example:
n = 10, I pick 6.

Return 6.

Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1


Constraints:

1 <= n <= 2^31 - 1
1 <= pick <= n

'''


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return n

        return self.guessNumberRec(1, n)

    def guessNumberRec(self, left, right):
        mid = (left + right) / 2
        ans = guess(mid)
        if ans == 0:
            return mid
        elif ans == 1:
            return self.guessNumberRec(mid + 1, right)
        elif ans == -1:
            return self.guessNumberRec(left, mid - 1)


    def guessNumber_iteration(self, n):
        """
        :type n: int
        :rtype: int
        """

        left = 0
        right = n

        while left <= right:

            mid = left + (right-left)//2
            ans = guess(mid)
            if ans == 0:
                return mid

            elif ans == 1:
                left = mid+1

            elif ans == -1:
                right = mid-1

        return -1