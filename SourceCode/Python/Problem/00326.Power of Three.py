'''
Level: Easy   Tag: [Math]

Given an integer,
write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true

Example 2:

Input: 0
Output: false

Example 3:

Input: 9
Output: true

Example 4:

Input: 45
Output: false

Follow up:
Could you do it without using any loop / recursion?

'''


class Solution(object):
    def __init__(self):
        self.k = 0

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        kkk = pow(3, self.k)

        if kkk == n:
            return True
        if kkk > n:
            return False
        self.k += 1
        return self.isPowerOfThree(n)


    def isPowerOfThreeNoRec(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # 1162261467 is largeset integer which can be divided by 3
        # Max integer is 2147483648

        return n > 0 and 1162261467 % n == 0

print(Solution().isPowerOfThree(1))