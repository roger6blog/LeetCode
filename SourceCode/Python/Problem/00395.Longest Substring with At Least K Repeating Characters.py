'''
Level: Medium

Find the length of the longest substring T of a given string (consists of lowercase letters only)

such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105
'''
import re

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        if len(s) < k:
            return 0
        charDic = {}
        for x in s:
            if x not in charDic:
                charDic[x] = 1
            else:
                charDic[x] += 1

        minChar = min(charDic, key=charDic.get)
        print(minChar)

        if s.count(minChar) >= k:
            return len(s)

        maxSubstring = 0
        for t in s.split(minChar):
            maxSubstring = max(maxSubstring, self.longestSubstring(t, k))

        return maxSubstring



    def longestSubstring2(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        from collections import deque, Counter


        count = Counter(s)
        queue = deque()
        max_len = float('-inf')
        for i in range(len(s)):
            if s[i] not in queue:
                if count[s[i]] >= k:
                    queue.append(s[i])
                else:
                    curr = Counter(queue)
                    while not all(v >= k for v in curr.values()) and len(queue) >0:
                        queue.popleft()
                        curr = Counter(queue)
            else:
                queue.append(s[i])

            curr = Counter(queue)
            if all(v >= k for v in curr.values()):
                max_len = max(max_len, len(queue))
            elif any(v>=k for v in curr.values()):
                max_repeat = 0
                t = "".join(queue)

                '''
                Compare two things and there is one relation between them:

                'a' == 'a'
                   True
                Compare three things, and there are two relations:

                'a' == 'a' == 'b'
                   True   False
                Combine these ideas - repeatedly compare things with the things next to them,
                and the chain gets shorter each time:

                'a' == 'a' == 'b'
                   True == False
                      False
                It takes one reduction for the 'b' comparison to be False,
                because there was one 'b'; two reductions for the 'a' comparison to be False
                because there were two 'a'. Keep repeating until the relations are all all False,
                and that is how many consecutive equal characters there were.
                '''
                while any(t):
                    t = [t[i] and t[i] == t[i+1] for i in range(len(t)-1)]
                    max_repeat += 1

                if max_repeat >= k:
                    max_len = max(max_len, max_repeat)

        print(max_len)
        return max_len



    def longestSubstring_rec(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        from collections import Counter

        if len(s) < k:
            return 0

        char_map = Counter(s)

        less_char = min(char_map, key=char_map.get)

        if s.count(less_char) >= k:
            return len(s)

        max_len = float('-inf')
        for t in s.split(less_char):
            max_len = max(max_len, self.longestSubstring_rec(t, k))

        return max_len

s = "bbaaacbd"
k = 3

# print(Solution().longestSubstring(s, k))
assert 3 == Solution().longestSubstring_rec(s, k)
s = "ababbc"
k = 2
assert 5 == Solution().longestSubstring_rec(s, k)

s = "a"
k = 2
assert 0 == Solution().longestSubstring_rec(s, k)

s = "baaabcb"
k = 3
assert 3 == Solution().longestSubstring_rec(s, k)


s = "ababacb"
k = 3
assert 0 == Solution().longestSubstring_rec(s, k)

s = "aaaaaaaaabbbcccccddddd"
k = 5
assert 10 == Solution().longestSubstring_rec(s, k)

s = "aaabbb"
k = 3
assert 6 == Solution().longestSubstring_rec(s, k)