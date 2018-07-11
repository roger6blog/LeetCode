

'''
Level: Hard Tag: [Sliding window]

Given a string S, find the length of the longest substring T that contains at most two distinct characters.
For example,
Given S = "eceba",
T is "ece" which its length is 3.

'''

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        left = 0 # left pointer of sliding window
        distinct = 0 # right pointer of sliding window, and count distinct char of string currently
        hashtable = [0 for i in xrange(256)] # total ASCII table char count
        longest = 0

        for i, char in enumerate(s):
            if hashtable[ord(char)] == 0:            
                distinct += 1
            
            hashtable[ord(char)] += 1
            
            # distinct > 2 means there is 3 char in current window
            # we should minus the word count of char of left pointer point
            # then delete char of left pointer point if count of char of hashtable is 0
            # so we can minus count of distinct char in current sliding window
            # then move left pointer to plus 1
            while distinct > 2:
                hashtable[ord(s[left])] -= 1
                if hashtable[ord(s[left])] == 0:
                    distinct -= 1
                left += 1
            longest = max(longest, i - left + 1)
        return longest

    
s = 'eceba'
sol = Solution()
print sol.lengthOfLongestSubstringTwoDistinct(s)
