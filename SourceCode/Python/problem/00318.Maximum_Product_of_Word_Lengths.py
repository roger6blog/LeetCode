'''

Given a string array words,

find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters.

You may assume that each word will contain only lower case letters.

If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".

Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".

Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.


'''


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        length = len(words)
        if length < 1:
            return 0
        maxProduct = 0
        lstWord = []
        for word in words:
            lstWord.append(set(word))

        for i in xrange(length):
            for j in xrange(length):
                if i != j:
                    if lstWord[i] & lstWord[j] == set([]):
                        maxProduct = max(maxProduct, len(words[i]) * len(words[j]))


        return maxProduct

words = ["abcw","baz","foo","bar","xtfn","abcdef"]
words2 = ["a","ab","abc","d","cd","bcd","abcd"]
words3 = ["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"]
print Solution().maxProduct(words3)