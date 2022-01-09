'''
Level: Medium

Given two integers dividend and divisor,

divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero,

which means losing its fractional part.

For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within

the 32-bit signed integer range: [-2^31, 2^31 - 1]. For this problem,

if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1,

and if the quotient is strictly less than -2^31, then return -2^31.



Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.


Constraints:

-2^31 <= dividend, divisor <= 2^31 - 1
divisor != 0

'''

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """


        x = abs(dividend)
        y = abs(divisor)
        ans = 0
        count = 1
        while x >= y:
            # 除數一直乘2
            y <<= 1

            if x >= y:
                # 乘完還是大於y的話, y繼續乘2, count也乘2
                count <<= 1

            else:
                # 乘完y比x大了, 退回一位讓x > y, 把count目前的數字加到ans去
                # 恢復原本的除數和count, 繼續循環
                y >>= 1
                x -= y
                ans += count
                y = abs(divisor)
                count = 1



        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            ans = -ans

        if ans >= 2**31:
            ans = 2**31-1

        if ans < -2**31:
            ans = -2**31

        print(ans)
        return ans


    def divide_TLE(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        ans = 0
        x = dividend
        y = divisor
        if x > 0:
            while x >= abs(y):
                x -= abs(y)
                ans += 1
        else:
            while abs(x) >= abs(y):
                x += abs(y)
                ans += 1

        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            ans = 0 - ans
        print(ans)
        return ans

# dividend = 10
# divisor = 3
# assert 3 == Solution().divide(dividend, divisor)

# dividend = 7
# divisor = -3
# assert -2 == Solution().divide(dividend, divisor)

# dividend = -7
# divisor = 3
# assert -2 == Solution().divide(dividend, divisor)

# dividend = 1
# divisor = 1
# assert 1 == Solution().divide(dividend, divisor)

# dividend = -1
# divisor = 1
# assert -1 == Solution().divide(dividend, divisor)

dividend = -2147483648
divisor = -1
assert 2147483647 == Solution().divide(dividend, divisor)

dividend = -2147483648
divisor = 1
assert -2147483648 == Solution().divide(dividend, divisor)