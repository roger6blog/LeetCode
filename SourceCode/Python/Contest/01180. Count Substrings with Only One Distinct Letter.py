'''
5067->1180. Count Substrings with Only One Distinct Letter
Difficulty: Easy
Given a string S, return the number of substrings that have only one distinct letter.



Example 1:

Input: S = "aaaba"
Output: 8
Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
"aaa" occurs 1 time.
"aa" occurs 2 times.
"a" occurs 4 times.
"b" occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.
Example 2:

Input: S = "aaaaaaaaaa"
Output: 55


Constraints:

1 <= S.length <= 1000
S[i] consists of only lowercase English letters.

'''

class Solution(object):
    def countLetters(self, S):
        """
        :type S: str
        :rtype: int
        """
        letters = {}
        curr = ''
        ans = 0
        for i, c in enumerate(S):
            if not curr:
                curr = c
            elif curr[-1] == c:
                # for i in range(len(curr)):
                #     letters[curr[:i+1]] += 1
                ans += len(curr)
                curr += c
            else:
                curr = c
            if curr not in letters:
                letters[curr] = 1
            else:
                letters[curr] += 1
        for k, v in letters.items():
            ans += v
        return ans


S = "aaaaaaaaaa"
print(Solution().countLetters(S))