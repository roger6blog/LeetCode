'''

5249->1249. Minimum Remove to Make Valid Parentheses

Difficulty: Medium
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')',
in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"


Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.

'''


class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """

        st = []
        dic = {}
        newstr = ''
        for i in range(len(s)):
            if s[i] == '(' or s[i] == ')':

                dic[i] = s[i]
                if len(st) == 0:
                    st.append((i, s[i]))
                else:
                    t = st[-1]
                    if s[i] == '(':
                        st.append((i, s[i]))
                    else:
                        if t[1] == '(':
                            st.pop()
                        else:
                            st.append((i, s[i]))

        s = list(s)
        while len(st) > 0:
            s[st[-1][0]] = '0'
            st.pop()

        newstr = ''.join(s).replace('0', '')



        return newstr

s = "lee(t(c)o)de)"
print(Solution().minRemoveToMakeValid(s))
