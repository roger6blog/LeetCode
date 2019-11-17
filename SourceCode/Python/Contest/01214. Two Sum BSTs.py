'''

5080->1214. Two Sum BSTs
Difficulty: Medium
Given two binary search trees,

return True if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.

Example 1:
(01214_1_b.png)

Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.

Example 2:
(01214_2_b.png)
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false


Constraints:

Each tree has at most 5000 nodes.
-10^9 <= target, node.val <= 10^9

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Definition for a binary tree node.
class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None



    def add(self, data):
        if self.val:
            if self.left is None:
                self.left = Node(data)
            else:
                if self.right is None:
                    self.right = Node(data)
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
    def inorderTraversal(self, root):
        return (self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)) if root else []

    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """
        lst1 = self.inorderTraversal(root1)
        lst2 = self.inorderTraversal(root2)

        s1 = set()
        for i in xrange(len(lst1)):
            s1.add(lst1[i])

        for j in xrange(len(lst2)):
            if (target-lst2[j]) in s1:
                return True
        return False

a = [-10,10]
tree1 = Node(0)
for i in a:
    tree1.add(i)


a = [1,7,0,2]
tree2 = Node(1)
for i in a:
    tree2.add(i)

target = 18
print(Solution().twoSumBSTs(tree1, tree2, 5))