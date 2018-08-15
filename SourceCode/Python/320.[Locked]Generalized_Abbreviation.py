'''

Write a function to generate the generalized abbreviations of a word.

Example:
Given word = "word", return the following list (order does not matter):
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

'''

class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        ans= []
        ans.append(word)
        self.dfs(0, word, ans)
        return ans

    def dfs(self, start, word, ans):
        if start >= len(word):
            return

        for i in xrange(start, len(word)):
            for j in xrange(1, len(word)):
                abbr = word[:i] + str(j) + word[i+j:]
                ans.append(abbr)
                self.dfs(i+1+j, abbr, ans)

word = "word"
print Solution().generateAbbreviations(word)