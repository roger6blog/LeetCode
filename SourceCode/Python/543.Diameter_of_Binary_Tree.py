'''

Given a binary tree,

you need to compute the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.

This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.


'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):

        if node.left is None:
            node.left = TreeNode(val)

        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._add(val, node.left)



class Solution(object):
    def __init__(self):
        self.maxLen = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.traversal(root.root)
        return self.maxLen

    def traversal(self, root):
        if not root:
            return 0

        left = self.traversal(root.left)
        right = self.traversal(root.right)

        self.maxLen = max(self.maxLen, int(left) + int(right))
        return max(left, right) + 1





a = [1,2,3,4,5]
tree = Tree()
for i in a:
    tree.add(i)
print Solution().diameterOfBinaryTree(tree)
