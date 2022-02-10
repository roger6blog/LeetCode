'''
Level: Medium   Tag: [String]

Given two strings s and t, return true if they are equal when both are typed into empty text editors.

'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.



Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.


Follow up: Can you solve it in O(n) time and O(1) space?


'''

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack_s = []
        stack_t = []
        for i in s:
            if i != "#":
                stack_s.append(i)
            else:
                if stack_s:
                    stack_s.pop()

        for i in t:
            if i != "#":
                stack_t.append(i)
            else:
                if stack_t:
                    stack_t.pop()

        return "".join(stack_s) == "".join(stack_t)

s = "ab#c"
t = "ad#c"
assert True == Solution().backspaceCompare(s, t)

s = "ab##"
t = "c#d#"
assert True == Solution().backspaceCompare(s, t)

s = "a#c"
t = "b"
assert False == Solution().backspaceCompare(s, t)