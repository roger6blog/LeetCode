'''

Given two non-negative integers num1 and num2 represented as string,

return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.

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

num1 = '12345'
num2 = '5678'
print Solution().addStrings(num1, num2)