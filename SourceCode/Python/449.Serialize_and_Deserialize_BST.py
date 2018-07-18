'''

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer,

or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree.

There is no restriction on how your serialization/deserialization algorithm should work.

You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states.

Your serialize and deserialize algorithms should be stateless.

'''



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# This soultion is same as 297.Serialize_and_Deserialize_Binary_Tree_accept totally
class Codec:
    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()

# Your Codec object will be instantiated and called as such:
#codec = Codec()
#print codec.deserialize(codec.serialize(tree.root))


