'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.


'''

class Solution:
    """
    @param words: a list of words
    @param word1: a string
    @param word2: a string
    @return: the shortest distance between word1 and word2 in the list
    """
    def shortestDistance(self, words, word1, word2):
        # Write your code here
        word_map = {}
        for c, w in enumerate(words):
            word_map[w] = c

        return abs(word_map[word1] - word_map[word2])


words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"

wordsb = ["practice", "makes", "perfect", "coding", "makes"]
word3 = "makes"
word4 = "coding"


print(Solution().shortestDistance(words, word1, word2))
print(Solution().shortestDistance(words, word3, word4))