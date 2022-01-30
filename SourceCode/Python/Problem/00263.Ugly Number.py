'''
Level: Easy  Tag: [Math]

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 * 3

Example 2:

Input: 8
Output: true
Explanation: 8 = 2 * 2 * 2

Example 3:

Input: 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:

1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [-2^31,  2^31 - 1].


Constraints:

-2^31 <= n <= 2^31 - 1
'''

class Solution(object):
    def isUgly_TLE(self, num):
        """
        :type num: int
        :rtype: bool
        """
        primes = [2, 3, 5]
        factor = []
        while num != 1:
            for i in xrange(2, num+1):
                if num % i ==0:
                    if i not in factor:
                        factor.append(i)
                    num = num / i
                    break

        for n in factor:
            if n not in primes:
                return False

        return True

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False

        primes = [2, 3, 5]

        for p in primes:
            while num % p == 0:
                num = num / p

        if num == 1:
            return True
        else:
            return False

num = 8
print(Solution().isUgly(num))