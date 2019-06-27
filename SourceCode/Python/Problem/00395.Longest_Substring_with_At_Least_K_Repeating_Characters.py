'''

Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.


'''
import re
import collections
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        if len(s) < k:
            return 0
        charDic = {}
        for x in s:
            if x not in charDic:
                charDic[x] = 1
            else:
                charDic[x] += 1

        minChar = min(charDic, key=charDic.get)
        print minChar

        if s.count(minChar) >= k:
            return len(s)

        maxSubstring = 0
        for t in s.split(minChar):
            maxSubstring = max(maxSubstring, self.longestSubstring(t, k))

        return maxSubstring



# s = "ababbc"
# k = 2
s = "bbaaacbd"
k = 3

print Solution().longestSubstring(s, k)