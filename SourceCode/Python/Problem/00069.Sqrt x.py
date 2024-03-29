'''
Level: Easy

Implement int sqrt(int x).

Compute and return the square root of x,

where x is guaranteed to be a non-negative integer.

Since the return type is an integer,

the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2


Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.



Constraints:

0 <= x <= 2^31 - 1

'''


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        left = 0
        right = x
        mid = (left + right) / 2
        while left <= right:
            if mid ** 2 > x:
                right = mid -1
            else:
                left = mid + 1
            mid = (left + right) / 2
        return mid



    def yourSqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        mid = (left + right) // 2
        while left <= right:

            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                right = mid - 1
            if mid ** 2 < x:
                left = mid + 1
            mid = (left + right) // 2
        print(mid)
        return mid


print(Solution().mySqrt(8))


assert 10 == Solution().yourSqrt(100)
assert 2 == Solution().yourSqrt(8)
assert 0 == Solution().yourSqrt(0)
assert 65535 == Solution().yourSqrt(2**32-1)