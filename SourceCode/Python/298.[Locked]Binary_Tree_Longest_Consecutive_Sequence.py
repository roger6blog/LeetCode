from binarytree import Node
'''

Given a binary tree, 

find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 

The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,
   1
    \
     3
    / \
   2   4
        \
         5
         
Longest consecutive sequence path is 3-4-5, so return 3.


   2
    \
     3
    / 
   2    
  / 
 1
 
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.


'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return max(self.longest(root.left, root.value), self.longest(root.right, root.value), self.longestConsecutive(root.left), self.longestConsecutive(root.right))

    def longest(self, root, value):
        if not root or root.value != value + 1:
            return 1

        return 1 + max(self.longest(root.right, root.value), self.longest(root.left, root.value))



root = Node(1)
root.right = Node(3)
root.right.left = Node(2)
root.right.right = Node(4)
root.right.right.right = Node(5)

root2 = Node(2)
root2.right = Node(3)
root2.right.left = Node(2)
root2.right.left.left = Node(1)
print root
print root2

print Solution().longestConsecutive(root)
print Solution().longestConsecutive(root2)