'''

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 <= k <= BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

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

class Solution(object):
    def __init__(self):
        self.count = 0
        self.ans = []
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        self.dfs(root, self.ans)
        self.ans.sort()
        #print self.count
        #print len(self.ans)
        #print self.ans
        if len(self.ans) < k-1:
            return self.ans[k-1-self.count]
        else:
            return self.ans[k-1]


    def dfs(self, Tree, ans):
        #print("Tree.val = {}".format(Tree.val))
        if Tree.val is not None:
            ans.append(Tree.val)
        else:
            self.count += 1
        if not Tree.left and not Tree.right:
            return



        if Tree.left:
            #print("Tree.left.val = {}".format(Tree.left.val))
            self.dfs(Tree.left, ans)
        if Tree.right:
            #print("Tree.right.val = {}".format(Tree.right.val))
            self.dfs(Tree.right, ans)


# Accepted by Leetcode as well, but has different answer in ordinary script
class Solution2(object):
    def kthSmallest(self, root, k):
        self.k = k
        self.res = None
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.helper(node.right)

a = [3,1,4,None,2]
k = 1
#a = [1,None,2]
#k = 2
tree = Tree()
for i in a:
    tree.add(i)

sol = Solution2()
x = sol.kthSmallest(tree.getRoot(), k)
print x


