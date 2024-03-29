'''
Level: Medium   Tag: [Stack]

You are given a nested list of integers nestedList.

Each element is either an integer or a list whose elements may also be integers or other lists.

Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
If res matches the expected flattened list, then your code will be judged as correct.


Example 1:

Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:

Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].


Constraints:

1 <= nestedList.length <= 500
The values of the integers in the nested list is in the range [-106, 106].



========== Old Description ============


Given a nested list of integers,
implement an iterator to flatten it.

Each element is either an integer, or a list --
whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,4,6].

'''


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer,
#         rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds,
#        if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds,
#        if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

import os
class NestedIterator(object):
    def __init__(self, nestedList):
        self.stack = []
        self.list = nestedList


    def isInteger(self, obj):
        if isinstance(obj, int):
            return True
        return False
    def next(self):
        return self.stack.pop(0)

    def hasNext(self):
        while self.list or self.stack:
            if not self.stack:
                self.stack.append(self.list.pop(0))
            while self.stack and not self.isInteger(self.stack[-1]):
                top = self.stack.pop()
                for e in top:
                    self.stack.append(e)
            if self.stack and self.isInteger(self.stack[-1]):
                return True
        return False







class NestedIterator2(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = nestedList[::-1]


    # @return {int} the next element in the iteration
    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()

    # 在while语句中查找拆解所有的list并按照顺序在next()中pop
    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            if self.stack[-1].isInteger():
                return True
            top = self.stack.pop()
            self.stack += top.getList()[::-1]
        return False








# Your NestedIterator object will be instantiated and called as such:
nestedList = [[1,1],2,[6,1]]
S
i, v = NestedIterator(nestedList), []
while i.hasNext():
    v.append(i.next())
print v

