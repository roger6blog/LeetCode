'''

Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

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

Input: columnTitle = "A"
Output: 1

Example 2:

Input: columnTitle = "AB"
Output: 28

Example 3:

Input: columnTitle = "ZY"
Output: 701


Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].


'''

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        letter_map = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans = 0
        for c, i in enumerate(list(columnTitle[::-1])):
            ans += letter_map.index(i) * 26 ** c

        print(ans)

        return ans


columnTitle = "ZY"
assert 701 == Solution().titleToNumber(columnTitle)

columnTitle = "FXSHRXW"
assert 2147483647 == Solution().titleToNumber(columnTitle)