'''
Level: Medium Tag: 2DP


Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.


Example 1:

"../../../Material/interleave.jpg"


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true


Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.


Follow up: Could you solve it using only O(s2.length) additional memory space?

'''


'''

設DP[i][j] 為是否可由s1的前i個字串和s2的前j的字串所組成 True為可以組成 False為不可組成
如果DP[i][j] 為True，代表 DP[i-1個長度的s1字串][j個長度的s1字串] 為True 而且s1 位置i後面的字串 s2 位置j後面的字串加起來可以組成s3剩下的字串
所以狀態轉移方程式為 DP[i][j] = True if DP[]

'''

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m = len(s1)
        n = len(s2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        dp[0][0] = True





s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"