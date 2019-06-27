'''

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.

'''


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly =[]
        p2 = 0
        p3 = 0
        p5 = 0
        ugly.append(1)
        for i in xrange(1, n):
            ugly.append(0)
            ugly[i] = min(ugly[p2]*2, ugly[p3]*3, ugly[p5]*5)
            if ugly[i] == ugly[p2] * 2:
                p2 += 1
            if ugly[i] == ugly[p3] * 3:
                p3 += 1
            if ugly[i] == ugly[p5] * 5:
                p5 += 1

        return ugly[-1]


n = 100
print Solution().nthUglyNumber(n)
