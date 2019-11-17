'''

5190->1190. Reverse Substrings Between Each Pair of Parentheses
Difficulty: Medium
Given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any bracket.





Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Example 4:

Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"


Constraints:

0 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It's guaranteed that all parentheses are balanced.


'''


class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import deque
        left = s.split('(')
        right = deque(left.pop().split(')'))
        result = right.popleft()
        result = result[::-1]
        for _ in range(len(left)):
            if len(left) and len(right):
                result = left.pop() + result + right.popleft()
            elif not len(right):
                result = left.pop()+ result[::-1].strip("(").strip(")")
            elif not len(left):
                result = result[::-1].strip("(").strip(")") + right.popleft()
            result = result[::-1]

        return result[::-1].replace("(", "").replace(")", "")




s = "sxmdll(q)eki(x)"
print(Solution().reverseParentheses(s))