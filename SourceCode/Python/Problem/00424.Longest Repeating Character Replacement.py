'''
Level: Medium

You are given a string s and an integer k.

You can choose any character of the string and change it to any other uppercase English character.

You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.



Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.


Constraints:

1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length


'''


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        from collections import Counter
        ans = 0
        i = 0
        n = len(s)
        for i in range(n):
            for j in range(i+1, n):
                substr = s[i:j+1]
                c = Counter(substr)
                if len(c) <= 2:
                    ans = max(ans, len(substr))

        print(ans)
        return ans


    def characterReplacement_deque(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        from collections import deque, Counter
        queue = deque()
        ans = 0
        for i in range(len(s)):
            queue.append(s[i])
            n = len(set(queue))
            if n == 1:
                ans = max(ans, len(queue))
            else:
                c = Counter(queue)
                x = c.most_common(1)[0][1]
                if len(queue) - x <= k:
                    ans = max(ans, len(queue))
                else:
                    queue.popleft()

        print(ans)
        return ans



# s = "ABAA"
# k = 0
# Solution().characterReplacement(s, k)

# s = "ABBB"
# k = 2
# Solution().characterReplacement(s, k)

s = "AABABBA"
k = 1
Solution().characterReplacement(s, k)

s = "ABAB"
k = 2
Solution().characterReplacement(s, k)