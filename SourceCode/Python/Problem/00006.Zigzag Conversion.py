'''
Level: Medium   Tag: [String]

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"


Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000

'''


"""
建立一个大小为 numRows 的字符串数组，为的就是把之字形的数组整个存进去，然后再把每一行的字符拼接起来，就是想要的结果了。
顺序就是按列进行遍历，首先前 numRows 个字符就是按顺序存在每行的第一个位置，然后就是 '之' 字形的连接位置了，
可以发现其实都是在行数区间 [1, numRows-2] 内，只要按顺序去取字符就可以了，最后把每行都拼接起来即为所求

"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= numRows or numRows <= 1:
            return s

        ans = [""] * numRows

        for i in range(len(s)):
            zig = i % (numRows + numRows - 2)
            if zig < numRows:
                ans[zig] += s[i]
            else:
                ans[numRows + numRows - 2 - zig] += s[i]

        ans = "".join(ans)
        print(ans)
        return ans



s = "PAYPALISHIRING"
numRows = 3
Solution().convert(s, numRows)