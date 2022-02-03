'''
Level: Medium   Tag: [Math]

Given a non-negative integer n,

count all numbers with unique digits, x, where 0 <= x < 10^n.

Example:
Given n = 2, return 91.
(The answer should be the total numbers in the range of 0 <= x < 100,
excluding [11,22,33,44,55,66,77,88,99])

Example 2:

Input: n = 0
Output: 1



Credits:
Special thanks to @memoryless for adding this problem and creating all test cases.


Constraints:

0 <= n <= 8
'''


class Solution(object):
    def countNumbersWithUniqueDigits_TLE(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        count = 0
        for i in xrange(10**n):
            if len(set(str(i))) == len(str(i)):
                count += 1

        return count


    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        nums = 1
        total = 1
        dp = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        for i in dp[:n]:
            nums *= i
            total += nums
        return total
n = 7
print Solution().countNumbersWithUniqueDigits(n)
print Solution().countNumbersWithUniqueDigits_TLE(n)