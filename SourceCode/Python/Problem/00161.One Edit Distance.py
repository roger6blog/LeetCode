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
        if len(s) > len(t):
            s, t = t, s
        s = sorted(s)
        t = sorted(t)
        for i in s:
            for j in range(len(t))[::-1]:
                if t[j] == i:
                    t.remove(t[j])


        return len(t) == 1
s = "aDb"
t = "adb"
assert True == Solution().isOneEditDistance(s, t)

s = "ab"
t = "ab"
assert False == Solution().isOneEditDistance(s, t)
