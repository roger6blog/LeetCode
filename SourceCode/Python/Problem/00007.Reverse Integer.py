'''
Level: Medium

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within
the 32-bit signed integer range: [-2^31,  2^31 - 1].

For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.

Constraints:
-2^31 <= x <= 2^31 - 1
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not (-2 ** 31 < x < 2 ** 31 - 1):
            return 0

        if x < 0:
            y = int(str(-x)[::-1]) * -1
        else:
            y = int(str(x)[::-1])

        if not (-2 ** 31 < y < 2 ** 31 - 1):
            return 0
        return y


    def reverse_str(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        if "-" not in str(x):
            y = int(str(x)[::-1])
        else:
            x = [v for v in x if v != "-"]
            x = "".join(x)
            y = int("-" + x[::-1])

        if not (-2 ** 31 < y < 2 ** 31 - 1):
            return 0
        print(y)
        return y

    def reverse_math(self, x):
        """
        :type x: int
        :rtype: int
        """
        import sys

        ans = 0
        negative = False
        if x < 0:
            x = -x
            negative = True
        while x != 0:
            ans = ans*10 + x%10
            x //= 10

        if negative:
            ans = -ans

        if not (-2 ** 31 < ans < 2 ** 31):
            return 0

        print(ans)
        return ans

x = 123
y = 1534236469
print(Solution().reverse(x))
x = -123
assert -321 == Solution().reverse_math(x)
x = 120
assert 21 == Solution().reverse_str(x)
x = 1534236469
assert 0 == Solution().reverse_math(x)

