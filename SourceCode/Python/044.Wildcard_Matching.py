
'''
Level:Hard

Given an input string (s) and a pattern (p),
implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z,
and characters like ? or *.

Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a',
which does not match 'b'.

Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence,
while the second '*' matches the substring "dce".

Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false

'''


class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    # @good solution! use 'aaaabaaaab' vs 'a*b*b' as an example
    def isMatch(self, s, p):
        pPointer = 0
        sPointer = 0
        starStringCover = 0
        star = -1  # -1 means not be used before
        while sPointer < len(s):
            # Condition 1: substr match pattern or pattern is '?'
            if pPointer < len(p) and (s[sPointer] == p[pPointer] or p[pPointer] == '?'):
                sPointer += 1
                pPointer += 1
                continue
            # Condition 2: pattern is '*', going to starString coverage
            if pPointer < len(p) and p[pPointer] == '*':
                star = pPointer
                pPointer += 1
                starStringCover = sPointer
                continue
            # Condition 3: extend starString coverage until next time match: substr match pattern
            if star != -1:
                pPointer = star + 1
                starStringCover += 1
                sPointer = starStringCover
                continue
            # return False if all 3 condition not fit, it means pattern is shorter than string
            return False

        # Handle empty string situation
        # s: '', p: '*'
        while pPointer < len(p) and p[pPointer] == '*':
            pPointer += 1

        # return True if all pattern was go through
        if pPointer == len(p):
            return True
        return False
s1 = 'aa'
p1 = 'a'
s = ""
p = "*"
sol = Solution()
ans = sol.isMatch(s, p)
print ans

