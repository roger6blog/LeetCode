'''

Given a list of unique words,

find all pairs of distinct indices (i, j) in the given list,

so that the concatenation of the two words,

i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

'''


class Solution(object):
    def palindromePairs_TLE(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        mapping = {}
        for c, x in enumerate(words):
            mapping[x] = c

        ans = []
        for i in xrange(len(words)):
            for j in xrange(len(words)):
                if i == j:
                    continue
                res = words[i] + words[j]
                if self.isPalindrome(res):
                    if [i, j] not in ans:
                        ans.append([i, j])

        return ans

    def isPalindrome(self, word):
        res = []
        stack = word
        mid = len(word)/2
        i = 0
        while i < mid:
            if word[i] != stack[-1]:
                return False
            i += 1
            stack = stack[:-1]
        return True

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        ans = set()
        mapping = {}
        for x, y in enumerate(words):
            mapping[y] = x


        for index, word in enumerate(words):
            if "" in mapping and word != "" and self.isPalindrome(word):
                ans.add((mapping[""], index))
                ans.add((index, mapping[""]))

            revWord = word[::-1]
            if revWord in mapping:
                revIndex = mapping[revWord]
                if revIndex != index:
                    ans.add((revIndex, index))
                    ans.add((index, revIndex))

            for j in xrange(1, len(word)):
                left = word[:j]
                revLeft = left[::-1]
                right = word[j:]
                revRight = right[::-1]

                if self.isPalindrome(left) and revRight in mapping:
                    print("{} is Palindrome and {} in words, it can concat string '{}'".format(left, words[mapping[revRight]], words[mapping[revRight]]+words[index]))
                    ans.add((mapping[revRight], index))
                if self.isPalindrome(right) and revLeft in mapping:
                    print("{} is Palindrome and {} in words, it can concat string '{}'".format(right,words[mapping[revLeft]], words[index]+words[mapping[revLeft]]))
                    ans.add((index, mapping[revLeft]))
        return list(ans)



words = ["abcd","dcba","lls","s","sssll"]
print Solution().palindromePairs(words)