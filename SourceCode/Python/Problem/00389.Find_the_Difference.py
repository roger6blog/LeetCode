'''

Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.

'''


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) == 0:
            return t
        elif len(t) == 0:
            return s
        lstT = list(t)
        lstS = list(s)
        while len(lstS) != 0:
            lstT.pop(lstT.index(lstS.pop()))
        return lstT.pop()

s = "abcd"
t = "abcde"
print Solution().findTheDifference(s, t)