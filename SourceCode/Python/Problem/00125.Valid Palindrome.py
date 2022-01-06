'''
Level: Easy

Given a string, determine if it is a palindrome,

considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true


Example 2:

Input: "race a car"
Output: false


'''


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.replace(":", "")
        s = s.replace(" ", "")
        s = s.replace(",", "")
        s = s.replace(".", "")
        s = s.replace("@", "")
        s = s.replace("#", "")
        s = s.replace("-", "")
        s = s.replace("?", "")
        s = s.replace("\\", "")
        s = s.replace("'", "")
        s = s.replace("\"", "")
        s = s.replace(";", "")
        s = s.replace("!", "")
        s = s.replace("(", "")
        s = s.replace(")", "")
        s = s.replace("`", "")

        s = s.lower()

        mid = len(s) / 2
        if len(s) % 2 == 0:
            i = 0
            mid -= 1
            while mid - i >= 0:
                if s[mid - i] != s[mid + i + 1]:
                    return False
                i += 1
        else:
            i = 1
            while mid - i >= 0:
                if s[mid - i] != s[mid + i]:
                    return False
                i += 1
        return True

    def isPalindrome2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        s = re.sub("[^a-zA-Z0-9]", "", s)

        s = s.lower()

        t = s[::-1]
        return t == s




s = "A man, a plan, a canal: Panama"
s1 = "abb"
print(Solution().isPalindrome2(s))

s = "race a car"
print(Solution().isPalindrome2(s))

s = "ab"
assert False == Solution().isPalindrome2(s)

s = "ab_a"
assert True == Solution().isPalindrome2(s)

s = "0P"
assert False == Solution().isPalindrome2(s)