'''

Given a string,

find the first non-repeating character in it and return it's index.

If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.


'''


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1
        sat = {}
        for i in s:
            if i not in sat:
                sat[i] = 1
            else:
                sat[i] += 1
        for c, i in enumerate(s):
            if sat[i] == 1:
                return c

        return -1


s = "loveleetcode"
print Solution().firstUniqChar(s)
