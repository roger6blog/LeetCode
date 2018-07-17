
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



    # Print the Tree inorder
    def printTreeInorder(self):
        if self.left:
            self.left.printTreeInorder()
        print(self.val),
        if self.right:
            self.right.printTreeInorder()

    # Print the Tree preorder
    def printTreePreorder(self):

        print(self.val),
        if self.left:
            self.left.printTreePreorder()
        if self.right:
            self.right.printTreePreorder()

    # Print the Tree postorder
    def printTreePostorder(self):
        if self.left:
            self.left.printTreePostorder()
        if self.right:
            self.right.printTreePostorder()
        print(self.val),


    # Inorder traversal
    # Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res = res + self.inorderTraversal(root.right)
        return res

    # Preorder traversal
    # Root -> Left ->Right
    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.val)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res


    # Postorder traversal
    # Left ->Right -> Root
    def postOrderTraversal(self, root):
        res = []
        if root:
            res = res + self.postOrderTraversal(root.left)
            res = res + self.postOrderTraversal(root.right)
            res.append(root.val)
        return res



tree = Node(27)
tree.add(14)
tree.add(35)
tree.add(10)
tree.add(19)
tree.add(31)
tree.add(42)

tree.printTreeInorder()
print "\n--------"
print tree.inorderTraversal(tree)
print "--------"
tree.printTreePreorder()
print "\n--------"
print tree.preorderTraversal(tree)
print "--------"
tree.printTreePostorder()
print "\n--------"
print tree.postOrderTraversal(tree)
