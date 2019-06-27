'''

Given a non-empty binary search tree and a target value,
find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.

'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def add(self, data):
        if self.val:
            if data < self.val:
                if self.left:
                    self.left.add(data)
                else:
                    self.left = TreeNode(data)
            elif data > self.val:
                if self.right:
                    self.right.add(data)
                else:
                    self.right = TreeNode(data)
        else:
            self.val = data

    # Print the Tree preorder
    def printTree(self):

        print(self.val),
        if self.left:
            self.left.printTree()
        #print( self.val),
        if self.right:
            self.right.printTree()



class Solution(object):
    def __init__(self):
        self.minVal = 0
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """

        if root is None:
            return None

        if target <= root.val:
            if root.left:
                leftClosestValue = self.closestValue(root.left, target)
                if root.val - target < abs(leftClosestValue - target):
                    return root.val
                else:
                    return leftClosestValue
        else:
            if root.right:
                rightClosetValue = self.closestValue(root.right, target)
                if root.val - target < abs(rightClosetValue - target):
                    return root.val
                else:
                    return rightClosetValue
            else:
                return root.val




a = [3,1,4,None,2]
tree = TreeNode(5)
for i in a:
    tree.add(i)
print tree.val
print "-------------"
tree.printTree()

print "\n-------------\n"
print Solution().closestValue(tree, 6)