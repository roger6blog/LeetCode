'''
Level: Medium

Given a string s, find the longest palindromic substring in s.

You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

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




    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def longestPalindrome_half(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left+1 : right]

        self.max_sub_str = ""

        for i in range(len(s)):
            odd = longestPalindrome_half(s, i, i)
            even = longestPalindrome_half(s, i, i+1)


            self.max_sub_str = max([self.max_sub_str, odd, even], key=len)

        print(self.max_sub_str)

        return self.max_sub_str

Input = "babad"
Output = "bab"
print(Solution().longestPalindrome(Input))