'''
Level: Medium

Implement pow(x, n),
which calculates x raised to the power n (x^n).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100

Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2^-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer,
within the range [-2^31, 2^31 - 1]


'''


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        y = 1
        if n < 0:
            x = 1/x
            n = -n

        while n > 0:
            if n % 2 != 0:
                y = y * x
            x = x * x
            n= n/2
        return y





    def yourPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        z = x ** n
        print(z)

x = 2
n = 10
Solution().myPow(x, n)

x = 2.00000
n = -2
Solution().yourPow(x, n)