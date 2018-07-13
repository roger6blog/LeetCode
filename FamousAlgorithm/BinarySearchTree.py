'''

Example 1:

Input: root = [3,1,4,null,2]
   3
  / \
 1   4
  \
   2

Example 2:

Input: root = [5,3,6,2,4,null,null,1]
       5
      / \
     3   6
    / \
   2   4
  /
 1


'''

# Definition for a binary search tree node.


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
        if val < node.val:
            if node.left:
                self._add(val, node.left)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self._add(val, node.right)
            else:
                node.right = TreeNode(val)


a = [3,1,4,None,2]
tree = Tree()
for i in a:
    tree.add(i)
print tree.getRoot().val