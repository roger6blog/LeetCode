'''
Given a string s, find the longest palindromic substring in s.

You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"


'''


class Solution(object):
    def longestPalindrome_Recursive(self, s):
        """
        :type s: str
        :rtype: str
        """
        def findPalindromeFrom(string, left, right):
            while left >= 0 and right < len(string) and string[left] == string[right]:
                left -= 1
                right += 1

            return string[left + 1:right]

        if not s:
            return ""

        longest = ""
        for mid in range(len(s)):
            sub = findPalindromeFrom(s, mid, mid)
            if len(sub) > len(longest):
                longest = sub

            sub = findPalindromeFrom(s, mid, mid + 1)
            if len(sub) > len(longest):
                longest = sub

        return longest




    def longestPalindrome_TLE(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s

        p = ''
        n = len(s)
        for l in range(n+1):
            for r in range(n+1):
                t = s[l:r]
                if t == t[::-1] and len(t) > len(p):
                    p = t

        return p




Input = "babad"
Output = "bab"
Solution().longestPalindrome_Recursive(Input)