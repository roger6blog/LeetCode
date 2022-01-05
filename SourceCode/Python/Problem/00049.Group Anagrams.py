'''
Level: Medium

Given an array of strings strs, group the anagrams together.

You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.


'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        maps = {}
        count = 0
        for word in strs:
            w = "".join(sorted(word))
            if w not in maps:
                maps[w] = count
                count += 1
        ans = []
        for _ in range(count):
            ans.append([])
        for word in strs:
            w = "".join(sorted(word))
            ans[maps[w]].append(word)
        print(ans)
        return ans











strs = ["eat","tea","tan","ate","nat","bat"]
[["bat"],["nat","tan"],["ate","eat","tea"]] == Solution().groupAnagrams(strs)