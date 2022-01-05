'''
Level: Easy

Given an integer columnNumber,

return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:

Input: columnNumber = 1
Output: "A"

Example 2:

Input: columnNumber = 28
Output: "AB"

Example 3:

Input: columnNumber = 701
Output: "ZY"


Constraints:

1 <= columnNumber <= 2^31 - 1

'''

class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        ans = []
        while columnNumber > 0:
            if columnNumber % 26 == 0:
                ans.append("Z")
                columnNumber -= 26
            else:
                ans.append(chr((columnNumber%26)+64))
            columnNumber //= 26

        ans = "".join(ans[::-1])
        print(ans)
        return ans

columnNumber = 701
assert "ZY" == Solution().convertToTitle(columnNumber)
columnNumber = 28
assert "AB" == Solution().convertToTitle(columnNumber)
columnNumber = 1
assert "A" == Solution().convertToTitle(columnNumber)
columnNumber = 2147483647
assert "FXSHRXW" == Solution().convertToTitle(columnNumber)
columnNumber = 52
assert "AZ" == Solution().convertToTitle(columnNumber)