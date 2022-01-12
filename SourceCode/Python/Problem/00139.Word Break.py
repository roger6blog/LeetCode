'''
Level: Medium

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.


'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # length of dp is 0,
        # it means the previous element was handle,
        # we can continue to parse from 0 now
        dp = [0]

        # the length of s, (1, len(s)+1)
        for i in xrange(1, len(s)+1):
            # All valid word break from beginning.
            # We cannot process behind string if we don't process front string
            # for loop: initial value = len(dp)-1, final value = -1, intervel = -1
            for j in xrange(len(dp)-1, -1, -1):
                substr = s[dp[j]: i]
                if substr in wordDict:
                    # Add dp record if substring in dict
                    dp.append(i)
                    break
        return dp[-1] == len(s)

    def wordBreak2(self, s, wordDict):
        # length of dp is 0,
        # it means the previous element was handle,
        # we can continue to parse from 0 now
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            # All valid word break from beginning.
            # We cannot process behind string if we don't process front string
            # for loop: initial value =i, final value = -1, intervel = -1
            for j in range(i):
                if dp[j] and s[j : i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]










    '''
    定义dfs
        递归的出口
        如果起始点已经在字符串的尾部
            停止，返回可以组成该字符串
        如果还未到结尾，枚举下一个字符串的长度。
            对于每种可能，判断该字符串是否在字典中
            如果在字典中：
                取出该字符串，判断剩下的是否可以
        找完所有可能后，仍然不行，直接返回这段字符串无法找到答案
    '''

    def wordBreak4_TLE(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        def rec(s, curr, memo):
            if curr in memo:
                return memo[curr]

            curr_len = len(curr)
            if curr_len > len(s):
                return False
            if curr == s:
                return True

            for w in wordDict:
                if w not in s:
                    continue
                if rec(s, curr+w, memo) == True:
                    return True
                else:
                    memo[curr+w] = False
            return False

        memo = {}
        a = rec(s, "", memo)
        return a



    '''

    設DP為s的前n個字元[0, n)能否由字典裡的字組成
    從一開始s的前0個字元開始比較
    如果前i個字元長度的字串[0, i)  扣掉當前比較字典裡的字的長度剩下的字串 之前的比較結果有符合
    當前比較的word長度的字串又有在字典內的話
    那前i個長度的字串就能被字典裡的字組成
    然後我們看題目要求的i個長度的字串結果是否能符合即為索求
    '''

    def wordBreak5(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        n = len(s)
        dp = [False] * (n+1)

        dp[0] = True

        for i in range(1, n+1):
            for word in wordDict:
                w = len(word)

                if dp[i-w] == True and s[i-w : i] in wordDict:
                    dp[i] = True
                    # 後面不用再找了 因為[0, i)的範圍已經可以被拆分了
                    break

        print(dp[n])
        return dp[n]

sol = Solution()
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
res = sol.wordBreak2(s, wordDict)
print res
res = sol.wordBreak("abcd", ["a","ab", "abc", "cde"])
print res

res = sol.wordBreak2("abcd", ["a","ab", "abc", "cde"])
print res


res = sol.wordBreak4_TLE("abcd", ["a","ab", "abc", "cde"])
print res

s = "applepenapple"
wordDict = ["apple", "pen"]
print(sol.wordBreak5(s, wordDict))

s = "bccdbacdbdacddabbaaaadababadad"
wordDict = ["cbc","bcda","adb","ddca","bad","bbb","dad","dac","ba","aa","bd","abab","bb","dbda","cb","caccc","d","dd","aadb","cc","b","bcc","bcd","cd","cbca","bbd","ddd","dabb","ab","acd","a","bbcc","cdcbd","cada","dbca","ac","abacd","cba","cdb","dbac","aada","cdcda","cdc","dbc","dbcb","bdb","ddbdd","cadaa","ddbc","babb"]

