'''
This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example, Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “makes”, word2 = “coding”, return 1. Given word1 = "makes", word2 = "makes", return 3.

Note: You may assume word1 and word2 are both in the list.


'''
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        from collections import defaultdict

        word_map = defaultdict(list)
        for c, w in enumerate(words):
            word_map[w].append(c)

        ans = len(words)
        for pos1 in word_map[word1]:
            word_map[word2] = word_map[word2][::-1]
            for pos2 in word_map[word2]:
                ans = min(ans, abs(pos1-pos2))
                if word1 == word2:
                    return ans

        return ans


class Solution2(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ans = float("inf")
        idx1 = idx2 = -1
        for i in range(0, len(words)):
            word = words[i]
            if word in (word1, word2):
                if word == word1:
                    idx1 = i
                    if idx2 != -1 and idx1 != idx2:
                        ans = min(ans, abs(idx2 - idx1))
                if word == word2:
                    idx2 = i
                    if idx1 != -1 and idx1 != idx2:
                        ans = min(ans, abs(idx2 - idx1))
        return ans

words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "coding"

print(Solution().shortestWordDistance(words, word1, word2))

word1 = "makes"
word2 = "makes"

print(Solution().shortestWordDistance(words, word1, word2))