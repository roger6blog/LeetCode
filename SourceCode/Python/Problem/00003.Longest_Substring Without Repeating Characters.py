'''
Level: Medium

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Explanation: The answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

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
        # ch in d, 当前字符在字典中，但是之前的ch也在字典中存在
        # 同时d[ch] >= start 说明字符所在的的位置必须在起始字符之后
        # 两个条件保证了获取到的子串的合理性
        for index, char in enumerate(s):
            # print "index = %d, char = %c" % (index, char)

            if char in wordDict and wordDict[char] >= begin:
                # 更新begin指向最新的位置
                begin = wordDict[char] + 1

            #  更新wordDict[char]的位置为index
            wordDict[char] = index

            # print "[%d, %d] -=> %s, length = %d" % (begin, index, s[begin:index + 1], index - begin + 1)

            maxLen = max(maxLen, len(s[begin:index])+1)
        return maxLen



    def lengthOfLongestSubstring_deque(self, s) :
        """
        :type s: str
        :rtype: int
        """
        from collections import deque
        if len(s) <= 1:
            return len(s)

        max_len = float('-inf')
        queue = deque()
        for i in range(len(s)):
            if s[i] not in queue:
                queue.append(s[i])
            else:
                if s[i] in queue:
                    while s[i] in queue:
                        queue.popleft()
                    queue.append(s[i])
                    continue
                while queue and queue[-1] != s[i]:
                    queue.pop()

            max_len = max(max_len, len(queue))

        print(max_len)
        return max_len












# s = "abba"
# print(Solution().lengthOfLongestSubstring("ababb"))
# print(Solution().lengthOfLongestSubstring(s))

s = "abcabcbb"
assert 3 == Solution().lengthOfLongestSubstring_deque(s)

s = "pwwkew"
assert 3 == Solution().lengthOfLongestSubstring_deque(s)

s = "bbbbb"
assert 1 == Solution().lengthOfLongestSubstring_deque(s)

s = "dvdf"
assert 3 == Solution().lengthOfLongestSubstring_deque(s)

s = "aabaab!bb"
assert 3 == Solution().lengthOfLongestSubstring_deque(s)