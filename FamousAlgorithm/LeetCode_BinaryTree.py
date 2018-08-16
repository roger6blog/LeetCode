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

# Definition for a binary tree node.
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


a = [3,1,4,None,2]
tree = TreeNode(5)
for i in a:
    tree.add(i)
print tree.val
print "-------------"
tree.printTree()