'''
Level: Easy

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.


Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.

Example 2:

Input: num = 0
Output: 0


Constraints:

0 <= num <= 2^31 - 1


'''

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0

        ans = 0
        while ans == 0 or num != 0:
            while num != 0:
                ans +=  num%10
                num //= 10
                print(ans)
            if num == 0 and ans >= 10:
                num = ans
                ans = 0


        return ans



num = 38
assert 2 == Solution().addDigits(num)

num = 0
assert 0 == Solution().addDigits(num)