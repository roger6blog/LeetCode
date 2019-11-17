'''

5232->1234. Replace the Substring for Balanced String
Difficulty: Medium
You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.

A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.

Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced.

Return 0 if the string is already balanced.



Example 1:

Input: s = "QWER"
Output: 0
Explanation: s is already balanced.
Example 2:

Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
Example 3:

Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER".
Example 4:

Input: s = "QQQQ"
Output: 3
Explanation: We can replace the last 3 'Q' to make s = "QWER".


Constraints:

1 <= s.length <= 10^5
s.length is a multiple of 4
s contains only 'Q', 'W', 'E' and 'R'.

'''


class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = []
        ans = 0
        q = s.count("Q")
        num.append(q)
        r = s.count("R")
        num.append(r)
        w = s.count("W")
        num.append(w)
        e = s.count("E")
        num.append(e)

        avg = sum(num) / 4
        for i in range(len(num)):
            ans += abs(avg - num[i])

        return ans/2


s = "WWEQERQWQWWRWWERQWEQ"
print(Solution().balancedString(s))