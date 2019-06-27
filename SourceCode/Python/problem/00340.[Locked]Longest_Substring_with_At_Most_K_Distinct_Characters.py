'''

Given a string,
find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = "eceba" and k = 2,

T is "ece" which its length is 3.

'''

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        left = 0
        distinct = 0
        hash = [0 for i in xrange(256)]
        longest = 0
        for i, j in enumerate(s):

            if hash[ord(j)] == 0:
                distinct += 1
            hash[ord(j)] += 1
            while distinct > k:

                hash[ord(s[left])] -= 1
                if hash[ord(s[left])] == 0:
                    distinct -= 1
                left += 1

            longest = max(longest, i-left+1)
        return longest





s = "eceba"
print Solution().lengthOfLongestSubstringKDistinct(s, 2)