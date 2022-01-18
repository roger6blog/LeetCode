'''
Level: Medium    Tag: [Matrix],  [DFS]

Given a nested list of integers,

return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: the list [[1,1],2,[1,1]],
Output: 10.
Explanation:
four 1's at depth 2, one 2 at depth 1, 4 * 1 * 2 + 1 * 2 * 1 = 10

Example 2:

Input: the list [1,[4,[6]]],
Output: 27.
Explanation:
one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4 * 2 + 6 * 3 = 27



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

class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):


        self.ans = 0
        depth = 1
        self.get_depth_sum(nestedList, depth)
        return self.ans


    def get_depth_sum(self, nestedList, depth):
        for i in nestedList:
            if i.isInteger():
                self.ans += depth * i.GetInteger()
            else:
                self.get_depth_sum(i.getList(), depth+1)