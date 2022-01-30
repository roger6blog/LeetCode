'''
Level: Medium  Tag: [Math]

An additive number is a string whose digits can form an additive sequence.

A valid additive sequence should contain at least three numbers.

Except for the first two numbers,
each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits, return true if it is an additive number or false otherwise.

Note: Numbers in the additive sequence cannot have leading zeros,
so sequence 1, 2, 03 or 1, 02, 3 is invalid.



Example 1:

Input: "112358"
Output: true
Explanation:
The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

Example 2:

Input: "199100199"
Output: true
Explanation:
The additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199


Constraints:

1 <= num.length <= 35
num consists only of digits.


Follow up: How would you handle overflow for very large input integers?

'''
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in range(n):
            x = num[0:i+1]
            if len(x) > 1 and x[0] == "0":
                break
            for j in range(i+1, n-1):
                y = num[i+1:j+1]
                if len(y) > 1 and y[0] == "0":
                    break
                print(x, y)
                d1 = int(x)
                d2 = int(y)
                d3 = str(int(d1) + int(d2))
                if d3 not in num[j+1:]:
                    continue

                additive = x + y + d3
                while len(additive) < len(num):
                    d1 = d2
                    d2 = int(d3)
                    d3 = str(d1 + d2)
                    additive += d3

                if additive == num:
                    return True
        return False



num = "199100199"
assert True == Solution().isAdditiveNumber(num)

num = "112358"
assert True == Solution().isAdditiveNumber(num)

num = "1023"
assert False == Solution().isAdditiveNumber(num)