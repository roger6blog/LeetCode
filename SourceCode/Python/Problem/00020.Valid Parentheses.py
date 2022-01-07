'''
Level: Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',

determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        par_map = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []
        if s.count("(") != s.count(")") or \
            s.count("[") != s.count("]") or \
                s.count("{") != s.count("}"):
                return False

        for i in s:
            if i in ["{", "[", "("]:
                stack.append(i)
            else:
                if par_map[i] not in stack:
                    return False
                if stack and stack[-1] == par_map[i]:
                    stack.pop()

        if stack:
            return False
        return True



s = "()[]{}"
assert True == Solution().isValid(s)

s = "()[{}"
assert False == Solution().isValid(s)

s = "[[[]"
assert False == Solution().isValid(s)

s = "]"
assert False == Solution().isValid(s)

s = "(([]){})"
assert True == Solution().isValid(s)
