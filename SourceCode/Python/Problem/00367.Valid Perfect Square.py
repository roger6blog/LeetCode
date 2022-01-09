'''
Level: Easy

Given a positive integer num,

write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.



Example 1:

Input: num = 16
Output: true

Example 2:

Input: num = 14
Output: false


Constraints:

1 <= num <= 2^31 - 1


'''
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        left = 1
        right = num
        mid = (left+right) // 2
        while left <= right:
            if mid ** 2 == num:
                return True
            if mid ** 2 < num:
                left = mid + 1
            if mid ** 2 > num:
                right = mid - 1
            mid = (left+right) // 2

        return False

num = 16
assert True == Solution().isPerfectSquare(num)

num = 14
assert False == Solution().isPerfectSquare(num)