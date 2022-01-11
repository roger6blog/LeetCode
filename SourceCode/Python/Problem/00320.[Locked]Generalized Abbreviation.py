'''
Level: Medium

Write a function to generate the generalized abbreviations of a word.
The two numbers after the abbreviation cannot be adjacent.

Example:
Given word = "word", return the following list (order does not matter):
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1",
"w1r1", "1o2", "2r1", "3d", "w3", "4"]

Example 2:

Input:
word = "today"
Output:
["1o1a1","1o1ay","1o2y","1o3","1od1y","1od2","1oda1","1oday","2d1y","2d2","2da1",
"2day","3a1","3ay","4y","5","t1d1y","t1d2","t1da1","t1day","t2a1","t2ay","t3y","t4",
"to1a1","to1ay","to2y","to3","tod1y","tod2","toda1","today"]

'''

class Solution(object):
    # This is wrong answer
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        ans= []
        ans.append(word)
        self.dfs(0, word, ans)
        return sorted(ans)

    def dfs(self, start, word, ans):
        if start >= len(word):
            return

        for i in xrange(start, len(word)):
            for j in xrange(1, len(word)):
                abbr = word[:i] + str(j) + word[i+j:]
                ans.append(abbr)
                self.dfs(i+1+j, abbr, ans)











    def generateAbbreviations2(self, word):
        """
        :type word: str
        :rtype: List[str]
        """


        def rec(res, index, word, curr, num):
            if index == len(word):
                if num > 0:
                    curr += str(num)
                res.append(curr)
                return

            # Index進行縮寫操作時
            rec(res, index+1, word, curr, num+1)
            if num > 0:
                curr += str(num) + word[index]
            else:
                curr += word[index]
            # Index不進行縮寫操作時
            rec(res, index+1, word, curr, 0)


        ans = []
        rec(ans, 0, word, "", 0)
        ans.sort()
        print(ans)

        return ans







word = "word"
print(Solution().generateAbbreviations(word))
print(Solution().generateAbbreviations2(word))
word = "today"
print(Solution().generateAbbreviations(word))
print(Solution().generateAbbreviations2(word))