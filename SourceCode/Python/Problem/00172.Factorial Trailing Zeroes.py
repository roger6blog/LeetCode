'''
Level: Medium   Tag: [Math]

Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.


Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:

Input: n = 0
Output: 0


Constraints:

0 <= n <= 10^4


Follow up: Could you write a solution that works in logarithmic time complexity?


'''
class Solution(object):
    def trailingZeroes_TLE(self, n):
        """
        :type n: int
        :rtype: int
        """
        fac = 1
        for i in range(n):
            fac *= (i+1)

        ans = 0
        while fac % 10 == 0:
            ans += 1
            fac /= 10

        print(ans)

        return ans


    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_zero = 0
        while n > 0:
            num_zero += n // 5
            n //= 5

        return num_zero

n = 5
Solution().trailingZeroes(n)