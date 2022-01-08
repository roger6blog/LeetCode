'''
Level: Medium

Given a string expression of numbers and operators,

return all possible results from computing all the different possible ways

to group numbers and operators.

You may return the answer in any order.


Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2

Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10


Constraints:

1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].


'''

class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        import operator
        oper_map = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul
            }
        cache = {}
        def compute(s):
            if s in cache:
                return cache[s]
            res = []
            if not any([s.count("-"), s.count("+"), s.count("*")]):
                res.append(int(s))
                return res

            for i in range(len(s)):
                if s[i] in "*-+":
                    left = compute(s[:i])  # left part of operator
                    right = compute(s[i+1:])  # right part of operator
                    for l in left:
                        for r in right:
                            res.append(oper_map[s[i]](l, r))
            cache[s] = res
            return res

        ans = compute(expression)
        print(ans)

        return ans





expression = "2-1-1"
Solution().diffWaysToCompute(expression)