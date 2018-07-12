'''

Given a string, we can "shift" each of its letter to its successive letter,
for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets,
group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Return:

{
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
}


Note: For the return value,
each inner list's elements must follow the lexicographic order.


'''


class Solution:
    # @param {string[]} strings
    # @return {string[][]}
    def groupStrings(self, strings):
        ans = {}
        for word in strings:
            hash = self.getHashOffset(word)
            if hash not in ans:
                ans[hash] = [word]
            else:
                ans[hash].append(word)

        ans.values().sort()
        return ans.values()



    def getHashOffset(self, word):
        hash = []
        for w in xrange(len(word) - 1):
            hash.append((ord(word[w+1]) - ord(word[w])) % 26)
        # List cannot be index of dictionary, so we return tuple to be index.
        return tuple(hash)

str = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
str2 = ['lpt', 'txb', 'qzq', 'sbs']
print Solution().groupStrings(str2)