'''
Level: Medium

Given a string s,

remove duplicate letters so that every letter appears once and only once.

You must make sure your result is the smallest in lexicographical order among all possible results.



Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"


Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.


Note: This question is the same as 1081:
https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

'''

'''
用Stack
每来一个字母, 先与栈顶比较（如果有的话）如果其字典序比当前栈顶元素的小，且栈顶元素后面还有，就pop掉
'''

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """


        stack = [s[0]]
        for i in range(1, len(s)):
            while len(stack) > 0 and ord(stack[-1]) > ord(s[i]) and stack[-1] in s[i+1:]:
                if s[i] in stack:
                    break
                stack.pop()
            if s[i] not in stack:
                stack.append(s[i])
        t = "".join(stack)

        return t





s = "cbacdcbc"
assert "acdb" == Solution().removeDuplicateLetters(s)
s = "bcabc"
assert "abc" == Solution().removeDuplicateLetters(s)
s = "abacb"
assert "abc" == Solution().removeDuplicateLetters(s)