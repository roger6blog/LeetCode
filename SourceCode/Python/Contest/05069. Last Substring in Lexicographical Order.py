'''
5069. Last Substring in Lexicographical Order

Difficulty: Hard
Given a string s, return the last substring of s in lexicographical order.



Example 1:

Input: "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".
Example 2:

Input: "leetcode"
Output: "tcode"


Note:

1 <= s.length <= 10^5
s contains only lowercase English letters.

'''


class Solution(object):
    def lastSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        char = []
        for i in range(122, 96, -1):
            char.append(chr(i))

        for c in char:
            if c in s:
                for i, j in enumerate(s):
                    if s[i] == c:
                        return(s[i:len(s)])

ss = "xbylisvborylklftlkcioajuxwdhahdgezvyjbgaznzayfwsaumeccpfwamfzmkinezzwobllyxktqeibfoupcpptncggrdqbkji"
print(Solution().lastSubstring(ss))