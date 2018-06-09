


'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

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
        
