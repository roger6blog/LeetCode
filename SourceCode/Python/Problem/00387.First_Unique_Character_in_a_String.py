'''
Level: Easy

Given a string,

find the first non-repeating character in it and return it's index.

If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Example 3:

Input: s = "aabb"
Output: -1

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




    def firstUniqChar2(self, s):
        """
        :type s: str
        :rtype: int
        """

        char = {}

        for i in range(len(s)):
            if s[i] not in char:
                char[s[i]] = i
            else:
                char[s[i]] = -1

        ans = float('inf')
        for k, v in char.items():
            if v != -1:
                ans = min(ans, v)

        if ans == float('inf'):
            ans = -1
        print(ans)
        return ans


s = "loveleetcode"
assert 2 == Solution().firstUniqChar2(s)
s = "aabb"
assert -1 == Solution().firstUniqChar2(s)
s = "leetcode"
assert 0 == Solution().firstUniqChar2(s)