'''
Level: Medium  Tag: [String]

Given two strings A and B,

find the minimum number of times A has to be repeated such that B is a substring of it.

If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times ("abcdabcdabcd"),

B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Example 2:

Input: a = "a", b = "aa"
Output: 2

Constraints:

1 <= a.length, b.length <= 10^4
a and b consist of lowercase English letters.


'''


class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        na = len(A)
        nb = len(B)
        # 為了確保左右各加一個a所以加2
        # 寫3是因為python迴圈只到3-1
        times = nb / na + 3

        for i in xrange(1, times):
            if B in A * i:
                return i

        return -1


A = "abcd"
B = "cdabcdab"
C = "a"
D = "a"*10000
print Solution().repeatedStringMatch(C, D)
