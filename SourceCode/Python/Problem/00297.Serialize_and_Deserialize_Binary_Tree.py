'''

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree.
There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example:

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"

Clarification: The above format is the same as how LeetCode serializes a binary tree.
You do not necessarily need to follow this format,
so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states.
Your serialize and deserialize algorithms should be stateless.


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
                self._add(val, node.right)
            else:
                node.right = TreeNode(val)
        else:
            node.left = TreeNode(val)

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        code = []
        if root:
            code.append(str(root.val))
        else:
            return ""
        if root.left:
            self.dfs(root.left, code)

        if root.right:
            self.dfs(root.right, code)

        return ''.join(code)

    def dfs(self, node, code):
        if node and node.val != "null":
            code.append(str(node.val))
        else:
            code.append("#")

        if node.left:
            self.dfs(node.left, code)

        if node.right:
            self.dfs(node.right, code)





    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        root = Tree()
        root.add(data[0])
        for i in xrange(1, len(data)):
            if i != "#":
                node = TreeNode(i)
            else:
                node = TreeNode("null")
            root.add(node)

        return root

# Your Codec object will be instantiated and called as such:

tree = Tree()
tree.add(1)
tree.add(2)
tree.add(3)
tree.add("null")
tree.add("null")
tree.add(4)
tree.add(5)


codec = Codec()
#print codec.deserialize(codec.serialize(tree.root))
data =  codec.serialize(tree.root)
print data
codec.deserialize(data)

