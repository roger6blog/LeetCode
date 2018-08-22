'''

Given a binary search tree with non-negative values,

find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
Note: There are at least two nodes in this BST.

'''

from binarytree import Node


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        lstTree = []
        self.addNoteToList(root, lstTree)
        lstTree.sort()
        minValue = sys.maxint
        for i in xrange(len(lstTree)-1):
            minValue = min(minValue, abs(lstTree[i+1] - lstTree[i]))

        return minValue

    def addNoteToList(self, root, lstTree):
        if not root:
            return
        lstTree.append(root.value)
        if root.left:
            self.addNoteToList(root.left, lstTree)
        if root.right:
            self.addNoteToList(root.right, lstTree)




root = Node(236)
root.left = Node(104)
root.right = Node(701)
root.left.right = Node(227)
root.right.right = Node(911)
print root
print Solution().getMinimumDifference(root)