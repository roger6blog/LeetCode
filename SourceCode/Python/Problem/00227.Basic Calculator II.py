'''
Level: Medium   Tag: [Stack]

Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2^31, 2^31 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().



Example 1:

Input: s = "3+2*2"
Output: 7

Example 2:

Input: s = " 3/2 "
Output: 1

Example 3:

Input: s = " 3+5 / 2 "
Output: 5


Constraints:

1 <= s.length <= 3 * 10^5
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 2^31 - 1].
The answer is guaranteed to fit in a 32-bit integer.

'''

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        op = "+"
        nums = 0
        stack = []
        for c in range(len(s)):
            if s[c].isdigit():
                nums = nums*10 + int(s[c])

            if s[c] != " " and not s[c].isdigit() or c == len(s)-1:
                if op == "+":
                    stack.append(nums)
                elif op == "-":
                    stack.append(-nums)
                elif op == "*":
                    op2 = stack.pop()
                    stack.append(nums * op2)
                elif op == "/":
                    op2 = stack.pop()
                    res = int(abs(op2)/nums)
                    if op2 < 0:
                        res *= -1
                    stack.append(res)
                op = s[c]
                nums = 0

        if nums != 0:
            stack.append(nums)

        ans = 0
        for s in stack:
            ans += s

        print(ans)

        return ans

s = "3+2*2"
assert 7 == Solution().calculate(s)


s = "3*2+2"
assert 8 == Solution().calculate(s)

s = " 3+5 / 2 "
assert 5 == Solution().calculate(s)

s = " 3/2 "
assert 1 == Solution().calculate(s)

s = "42"
assert 42 == Solution().calculate(s)

s = "14-3/2"
assert 13 == Solution().calculate(s)