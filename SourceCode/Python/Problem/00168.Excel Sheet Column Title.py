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
        while columnNumber > 26:
            w = columnNumber % 26
            ans.append(chr(w+65))
            columnNumber = columnNumber % 26
        ans.append(chr(columnNumber+65))
        print(ans)
        return "".join(ans)

columnNumber = 701
assert "ZY" == Solution().convertToTitle(columnNumber)
columnNumber = 28
assert "AB" == Solution().convertToTitle(columnNumber)