'''

Given two non-negative integers num1 and num2 represented as strings,

return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.



Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"


Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.


'''

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        ans = 0
        for i in range(len(num2))[::-1]:
            for j in range(len(num1))[::-1]:
                ans += int(num1[j]) * (10 ** (len(num1) - (j+1))) * int(num2[i]) * (10 ** (len(num2) - (i+1)))

        print(ans)
        return str(ans)

num1 = "123"
num2 = "456"
assert "56088" == Solution().multiply(num1, num2)

num1 = "9"
num2 = "99"
assert "891" == Solution().multiply(num1, num2)