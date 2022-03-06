'''
Level: Easy

Given two non-negative integers num1 and num2 represented as string,

return the sum of num1 and num2.

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"


Constraints:

1 <= num1.length, num2.length <= 10^4
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.


!!!!!!!!!!!!!!!
You must not use any built-in BigInteger library or convert the inputs to integer directly.
eg, int() or str()
!!!!!!!!!!!!!!!

'''


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        def str2int(num):
            return ord(num) - ord('0')

        x = 0
        for i in xrange(len(num1)):
            x = x + 10**(len(num1)-i-1) * str2int(num1[i])

        y = 0
        for j in xrange(len(num2)):
            y = y + 10**(len(num2)-j-1) * str2int(num2[j])

        return str(x + y)




    def addStrings2(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def str2int(s):
            return ord(s) - ord('0')
        m = len(num1)
        n = len(num2)
        n1 = 0
        n2 = 0
        for i in range(m):
            n1 += str2int(num1[i]) * 10 ** (m-i-1)

        for i in range(n):
            n2 += str2int(num2[i]) * 10 ** (n-i-1)

        return str(n1+n2)

num1 = '12345'
num2 = '5678'
print Solution().addStrings2(num1, num2)