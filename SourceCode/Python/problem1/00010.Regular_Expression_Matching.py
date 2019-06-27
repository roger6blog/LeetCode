'''

Given an input string (s) and a pattern (p),
implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z,
and characters like . or *.

Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'.
Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time.
Therefore it matches "aab".

Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false


'''


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = []
        for x in xrange(len(s) + 1):
            dp.append([])
            for y in xrange(len(p) + 1):
                dp[x].append(False)

        dp[0][0] = True

        # Handle the scenario: "aab", "c*a*b"
        for i in xrange(len(p)):
            if p[i] == "*" and dp[0][i-1] == True:
                dp[0][i+1] = True

        for sp in xrange(1, len(s)+1):
            for pp in xrange(1, len(p)+1):
                if p[pp-1] == "*":
                    if dp[sp][pp-1] == True or \
                       dp[sp][pp-2] == True or \
                      (dp[sp-1][pp] == True and (s[sp-1] == p[pp-2] or p[pp-2] == '.')):
                        # 1. dp[sp][pp-1]: xa match xa*
                        # 2. dp[sp][pp-2]: x match xa*
                        # 3. dp[sp-1][pp] == True and s[sp-1] == p[pp-2]: xaa match xa*
                        dp[sp][pp] = True
                elif s[sp-1] == p[pp-1] or p[pp-1] == '.':
                    dp[sp][pp] = dp[sp-1][pp-1]

        return dp[len(s)][len(p)]
# s = "mississippi"
# p = "mis*is*p*."

s1 = "ab"
p1 = ".*"
s = "xaabyc"
p = "xa*b.c"

s3 = "aab"
p3 = "c*a*b"
print Solution().isMatch(s, p)