'''
5099->1216. Valid Palindrome III
Difficulty: Hard
Given a string s and an integer k, find out if the given string is a K-Palindrome or not.

A string is K-Palindrome if it can be transformed into a palindrome by removing at most k characters from it.


Example 1:

Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.


Constraints:

1 <= s.length <= 1000
s has only lowercase English letters.
1 <= k <= s.length

'''




class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """

        n = len(s)
        rev = s[::-1]
        tmp = []
        for _ in range(n+1):
            tmp.append([0] * (n+1))

        for x in range(n+1):
            for y in range(n+1):
                if not x or not y:
                    tmp[x][y] = 0
                elif s[x - 1] == rev[y - 1]:
                    tmp[x][y] = tmp[x - 1][y - 1] + 1
                else:
                    tmp[x][y] = max(tmp[x - 1][y], tmp[x][y - 1])

        if (n - tmp[n][n] ) <= k:
            return True
        else:
            return False

s = "abcdeca"
k = 2
print(Solution().isValidPalindrome(s, k))