'''
Level: Medium

Given a string,
find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = "eceba" and k = 2,

T is "ece" which its length is 3.

Example 2:

Input: S = "WORLD" and k = 4
Output: 4
Explanation: T = "WORL" or "ORLD"

Example 3:

Input: S = "eceba" and k = 3
Output: 4
Explanation: T = "eceb"
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







    def lengthOfLongestSubstringKDistinct_deque(self, s, k):
        from collections import deque, Counter
        if len(s) <= 1:
            return len(s)
        queue = deque()

        max_len = float('-inf')
        for i in range(len(s)):
            if s[i] not in queue :
                if len(Counter(queue)) < k:
                    queue.append(s[i])
                else:
                    while len(Counter(queue)) > k:
                        queue.popleft()

            else:
                queue.append(s[i])

            max_len = max(max_len, len(queue))

        print(max_len)
        return max_len

s = "eceba"
print(Solution().lengthOfLongestSubstringKDistinct(s, 2))


assert 3 == Solution().lengthOfLongestSubstringKDistinct_deque(s, 2)

assert 4 == Solution().lengthOfLongestSubstringKDistinct_deque(s, 3)
S = "WORLD"
k = 4
assert 4 == Solution().lengthOfLongestSubstringKDistinct_deque(S, k)