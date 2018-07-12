

'''
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
        for i in range(len(s)):
            # All valid word break from beginning.
            # We cannot process behind string if we don't process front string
            # for loop: initial value =i, final value = -1, intervel = -1
            for j in range(i, -1, -1):
                if dp[j] and s[j:i + 1] in wordDict:
                    dp[i + 1] = True
                    break
        return dp[len(s)]

sol = Solution()      
res = sol.wordBreak("abcd", ["a","ab", "abc", "cde"])
print res      
     
res = sol.wordBreak2("abcd", ["a","ab", "abc", "cde"])
print res      

      
