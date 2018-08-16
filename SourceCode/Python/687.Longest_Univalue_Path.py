'''

Given a binary tree,

find the length of the longest path where each node in the path has the same value.

This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:
2

Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:
2

Note:
The given binary tree has not more than 10000 nodes.

The height of the tree is not more than 1000.

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def add(self, data):
        if self.val:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.left.add(data)



    # Print the Tree preorder
    def printTree(self):

        print(self.val),
        if self.left:
            self.left.printTree()
        #print( self.val),
        if self.right:
            self.right.printTree()

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """


a = [3,1,4,None,2]
tree = TreeNode(5)
for i in a:
    tree.add(i)
print tree.val
print "-------------"
tree.printTree()