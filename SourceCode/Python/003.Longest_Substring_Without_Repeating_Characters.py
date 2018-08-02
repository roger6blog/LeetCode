'''

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


'''

class Solution(object) :
    def lengthOfLongestSubstring(self, s) :
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        begin = 0
        wordDict = {}
        maxLen = 0
        for index, char in enumerate(s):
            if char in wordDict and wordDict[char] >= begin:
                begin = wordDict[char] + 1
            wordDict[char] = index

            maxLen = max(maxLen, len(s[begin:index])+1)
        return maxLen

s = "abba"
print Solution().lengthOfLongestSubstring("ababb")
print Solution().lengthOfLongestSubstring(s)