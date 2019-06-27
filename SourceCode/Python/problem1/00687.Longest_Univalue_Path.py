import binarytree
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


class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return max(self.longestPath(root.left, root.value) + self.longestPath(root.right, root.value), \
                   self.longestUnivaluePath(root.left), \
                   self.longestUnivaluePath(root.right)
                   )

    def longestPath(self, root, value):
        if not root or root.value != value:
            return 0

        return 1 + max(self.longestPath(root.left, value), self.longestPath(root.right, value))



root = binarytree.Node(5)
root.left = binarytree.Node(4)
root.right = binarytree.Node(5)
root.left.left = binarytree.Node(1)
root.left.right = binarytree.Node(1)
root.right.right = binarytree.Node(5)
print root


root2 = binarytree.Node(1)
root2.left = binarytree.Node(4)
root2.right = binarytree.Node(5)
root2.left.left = binarytree.Node(4)
root2.left.right = binarytree.Node(4)
root2.left.right.right = binarytree.Node(4)
root2.right.right = binarytree.Node(5)
root2.right.right.right = binarytree.Node(5)
print root2
print Solution().longestUnivaluePath(root)
print Solution().longestUnivaluePath(root2)