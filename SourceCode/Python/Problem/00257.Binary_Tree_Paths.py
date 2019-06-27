'''

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

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
        if node.left:
            if node.right:
                self._add(val, node.left)
            else:
                node.right = TreeNode(val)
        else:
            node.left = TreeNode(val)


class Solution(object):
    def __init__(self):
        self.res = []
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        visited = []

        self.dfs(root, visited)
        return self.res

    def dfs(self, node, visited):
        if not node:
            return
        visited.append(str(node.val))
        if node.left is None and node.right is None:
            self.res.append('->'.join(visited))

        if node.left:
            self.dfs(node.left, visited)
        if node.right:
            self.dfs(node.right, visited)

        visited.pop()




a = [1, 2, 3, None, 5]
tree = Tree()
for i in a:
    tree.add(i)
print tree.getRoot().val
print Solution().binaryTreePaths(tree.getRoot())