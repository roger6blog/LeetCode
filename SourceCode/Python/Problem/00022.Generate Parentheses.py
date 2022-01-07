'''
Level: Medium

Given n pairs of parentheses,
write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
'''


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(left, right ,item, ans):
            if right < left:
                return
            if left == 0 and right == 0:
                ans.append(item)

            if left > 0:
                dfs(left-1, right, item+'(', ans)
            if right > 0:
                dfs(left, right-1, item+')', ans)



        ans = []
        dfs(n, n, '', ans)
        return ans




    def generateParenthesis2(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def add_parenthe(res, sub_str, left_paren_num, index, n):
            if index == n:
                while left_paren_num > 0:
                    sub_str += ")"
                    left_paren_num -= 1
                res.append(sub_str)
                return

            if left_paren_num > 0:
                add_parenthe(res, sub_str+")", left_paren_num-1, index, n)

            add_parenthe(res, sub_str+"(", left_paren_num+1, index+1, n)

        ans = []
        add_parenthe(ans, "", 0, 0, n)
        print(ans)
        return ans


n = 3
Solution().generateParenthesis2(n)