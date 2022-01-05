'''
Level: Easy

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.



Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false


Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.

'''


class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        dict_p = {}
        dict_w = {}

        words = s.split(" ")
        if len(words) != len(pattern):
            return False

        for w in range(len(words)):
            if words[w] not in dict_w:
                dict_w[words[w]] = pattern[w]
            else:
                if dict_w[words[w]] != pattern[w]:
                    return False

            if pattern[w] not in dict_p:
                dict_p[pattern[w]] = words[w]
            else:
                if dict_p[pattern[w]] != words[w]:
                    return False
        return True




pattern = "abba"
s = "dog cat cat dog"
assert True == Solution().wordPattern(pattern, s)

pattern = "abba"
s = "dog cat cat fish"
assert False == Solution().wordPattern(pattern, s)

pattern = "aaaa"
s = "dog cat cat dog"
assert False == Solution().wordPattern(pattern, s)

pattern = "abba"
s = "dog dog dog dog"
assert False == Solution().wordPattern(pattern, s)