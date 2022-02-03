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


'''
如果n = 1，那么可以有10个数字不同（0～9）
如果n >= 2，那么第一位可以是1～9共9个数字，第二位可以是出去第一位的数字+0共9个数字，
    之后的每位数字都必须不能使用前面已经用过的数字所以依次递减。即9,9,8,7,…,1
n位数字中由不同的数字构成的数字，是比它小的各位数字所能构成的该条件的数字求和。
使用循环求解，根据数字的位数，来求这个位数的能够满足条件的个数。ans是小于等于n位的求和。

如果看不明白代码，可以这么理解:
题目要求的是0 ≤ x < 10^n的x个数，那么x可以为1位数，2位数……n位数。
当x为1位数的时候有10个结果；当x为2位数的时候，有99个结果；
当x为3位数的时候，有998个结果……
也就是说当x为n位数的时候，有99*…*(11 - n个结果)，其中n必须小于等于10了（11位数字不可能每一位都不相同）。
最后求和就好

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


    def countNumbersWithUniqueDigits2(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 1

        nums = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        product = 1
        ans = 1
        for i in range(min(n, 10)):
            product *= nums[i]
            ans += product

        print(ans)
        return ans


n = 7
print(Solution().countNumbersWithUniqueDigits(n))
print(Solution().countNumbersWithUniqueDigits_TLE(n))
print(Solution().countNumbersWithUniqueDigits2(n))