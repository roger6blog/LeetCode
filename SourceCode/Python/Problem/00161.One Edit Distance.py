'''
Level: Medium

Given two strings S and T, determine if they are both one edit distance apart.
One ediit distance means doing one of these operation:

insert one character in any position of S
delete one character in S
change one character in S to other character

Example 1:

Input: s = "aDb", t = "adb"
Output: true
Example 2:

Input: s = "ab", t = "ab"
Output: false
Explanation:
s=t ,so they aren't one edit distance apart

'''
class Solution:
    def isOneEditDistance(self, s, t):
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """