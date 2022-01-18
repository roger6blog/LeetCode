'''
Level: Medium    Tag: [Matrix],  [DFS]

Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf,

now the weight is defined from bottom up. i.e., the leaf level integers have weight 1,

and the root level integers have the largest weight.


Example 1:

Input: nestedList = [[1,1],2,[1,1]]
Output: 8
Explanation:
four 1's at depth 1, one 2 at depth 2


Example 2:

Input: nestedList = [1,[4,[6]]]
Output: 17
Explanation:
one 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17


'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
   def isInteger(self):
       """
       @return {boolean} True if this NestedInteger holds a single integer,
       rather than a nested list.
       """

   def getInteger(self):
       """
       @return {int} the single integer that this NestedInteger holds,
       if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self):
       """
       @return {NestedInteger[]} the nested list that this NestedInteger holds,
       if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

'''

用DFS一邊統計每一層的深度，一邊把每層的數字都加到依層數設計的stack裏
跑完一遍後我們就可以確定這nestlist的深入
再把stack裡的個元素依層數乘上加權後全部累加即為所求
'''


class Solution:
    """
    @param nestedList: a list of NestedInteger
    @return: the sum
    """
    def depthSumInverse(self, nestedList):
        # Write your code here.
        self.ans = 0
        self.depth = 0
        stack = [0]
        self.get_sum_depth(nestedList, 0, stack)
        ans = 0
        for i in range(len(stack)):
            ans += stack.pop() * (i+1)

        print(ans)
        return ans

    def get_sum_depth(self, nestedList, level, stack):
        if level > len(stack):
            stack += [0]
        self.depth = max(self.depth, level)
        for i in nestedList:
            if i.isInteger():
                stack[level] += i.GetInteger()
            else:
                self.get_sum_depth(i.getList(), level+1, stack)