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


a = [3,1,4,None,2]
tree = Node(5)
for i in a:
    tree.add(i)
print tree.val
print "-------------"
tree.printTree()