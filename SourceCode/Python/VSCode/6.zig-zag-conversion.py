#
# @lc app=leetcode id=6 lang=python
#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (32.58%)
# Total Accepted:    339.8K
# Total Submissions: 1M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
#
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a
# number of rows:
#
#
# string convert(string s, int numRows);
#
# Example 1:

#
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#
#
# Example 2:
#
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#
#


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        if len(s) == 1:
            return s
        n = len(s)
        zigzag_arr = [['' for _ in range(numRows)] for _ in range(n/2+1)]
        direction = True
        x = 0
        while x <= n/2:
            if s == "":
                break
            if direction:
                for y in range(numRows-1, -1, -1):
                    zigzag_arr[x][y] = s[0]
                    s = s[1:]
                    if s == "":
                        break
                else:
                    direction = False
            else:
                for y in range(1, numRows-1):
                    x += 1
                    zigzag_arr[x][y] = s[0]
                    s = s[1:]
                    if s == '':
                        break
                else:
                    x += 1
                    direction = True

        return "".join(map("".join, zip(*zigzag_arr))[::-1])




# print Solution().convert("PAYPALISHIRING", 4)
# print Solution().convert("ABC", 2)

