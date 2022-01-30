'''
Level: Easy  Tag: [Math]

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.



Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:

Input: n = 2
Output: false


Constraints:

1 <= n <= 2^31 - 1

'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        repeat = []
        while n != 1:
            s = str(n)
            x = 0
            for i in s:
                x += int(i) ** 2
            if x in repeat:
                return False
            repeat.append(x)
            n = x
        if n == 1:
            return True

        return False

# n = 19
# assert True == Solution().isHappy(n)

n = 17
assert False == Solution().isHappy(n)

n = 7
Solution().isHappy(n)
