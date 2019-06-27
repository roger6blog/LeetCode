'''

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.


'''


import sys
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""

        if len(strs) == 1:
            return strs.pop()

        minstr = ""
        minlen = sys.maxint
        for s in strs:
            minlen = min(minlen, len(s))
            if minlen == len(s):
                minstr = s


        ans = ""
        for i in xrange(minlen):
            for s in strs:
                if s != strs[0] and s[i] != minstr[i]:
                    return ans

            ans += minstr[i]

        return ans

# s = ["flower","flow","flight"]
# s = ["dog","racecar","car"]
# s = ["aa","ab"]
s = ["c","c"]
print Solution().longestCommonPrefix(s)