'''
5052. Maximum Level Sum of a Binary Tree

Difficulty: Medium
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.



Example 1:



Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.


Note:

The number of nodes in the given tree is between 1 and 10^4.
-10^5 <= node.val <= 10^5

'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.level_sum = []
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sum_lvl(self, root, lvl):
            if root is None:
                return

            if self.level_sum != []:
                if len(self.level_sum) > lvl:
                    self.level_sum[lvl] += root.val
                else:
                    self.level_sum.append(root.val)
            else:
                 self.level_sum.append(root.val)
            lvl += 1
            sum_lvl(self, root.left, lvl)
            sum_lvl(self, root.right, lvl)

        sum_lvl(self, root, 0)
        return (self.level_sum.index(max(self.level_sum))+1)





null = None

tree = [1,7,0,7,-8,null,null]
a = TreeNode(tree[0])
b = TreeNode(tree[1])
c = TreeNode(tree[2])
a.left = b
a.right = c
b.left = TreeNode(tree[3])
b.right = TreeNode(tree[4])


print(Solution().maxLevelSum(a))