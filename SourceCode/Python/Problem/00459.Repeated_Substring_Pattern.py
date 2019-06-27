'''

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.


Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:

Input: "aba"
Output: False

Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)


'''
import unittest

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return False

        length = len(s)
        pos = length / 2
        while pos > 0:
            substr = s[:pos]
            div = length / pos
            if substr * div == s:
                return True
            else:
                div += 1
                pos = length / div

        return False

class TestrepeatedSubstringPattern(unittest.TestCase):
    def setup(self):
        pass

    def testPostive(self):
        s = "abcabcabcabc"
        self.assertTrue(Solution().repeatedSubstringPattern(s))
        s = "abaababaab"
        self.assertTrue(Solution().repeatedSubstringPattern(s))

    def testNegative(self):
        s = "aba"
        self.assertFalse(Solution().repeatedSubstringPattern(s))
        s = "aabaaba"
        self.assertFalse(Solution().repeatedSubstringPattern(s))

if __name__ == '__main__':
    unittest.main()
    # s = "abcabcabcabc"
    # print Solution().repeatedSubstringPattern(s)
