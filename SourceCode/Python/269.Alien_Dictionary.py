'''

There is a new alien language which uses the latin alphabet.
However, the order among letters are unknown to you.
You receive a list of words from the dictionary,
where words are sorted lexicographically by the rules of this new language.
Derive the order of letters in this language.

For example,
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]


The correct order is: "wertf".

Note:

You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.


'''
import collections


# BFS solution.
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        dqueue = collections.deque()
        nodes = set()
        for word in words:
            for c in word:
                nodes.add(c)

        print

input = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

print Solution().alienOrder(input)