

'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]

'''


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.ans = []
        self.dfs(s, wordDict, '')
        return self.ans
      
    def isWordBreak(self, s, wordDict):
        # length of dp is 0, it means the previous element was handle,
        # we can continue to parse from 0 now
        dp = [False for i in xrange(len(s)+1)]
        dp[0] = True

        for i in xrange(len(s)):
            # All valid word break from beginning.
            # We cannot process behind string if we don't process front string
            # for loop: initial value =i, final value = -1, intervel = -1            
            for j in xrange(i, -1, -1):
                if dp[j] and s[j:i+1] in wordDict:
                    dp[i+1] = True
                    break
        return dp[len(s)]

    def dfs(self, s, wordDict, stringlist):
        # Check if the word can be break into word in dictionary
        # We call this to reduce space requirement of DFS
        if self.isWordBreak(s, wordDict):
            if len(s) == 0:
                # Trace to end side, so process is complete
                self.ans.append(stringlist[1:])

            for i in xrange(1, len(s)+1):
                # If left side of word in dictionary
                if s[:i] in wordDict:
                    # Leetcode will occur Memory Exceed problem for this statement
                    #stringlist = ''.join([stringlist, ' ', s[:i]])
                    
                    # Add right side to check word break in DFS
                    self.dfs(s[i:], wordDict, stringlist+' '+s[:i])
            
sol = Solution()
res = sol.wordBreak("abcd", ["a", "ab", "abc", "cd", "d"])
print res
