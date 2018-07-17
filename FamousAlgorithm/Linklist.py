
# Creation of Linked list
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class Linklist:
    def __init__(self):
        self.head = None

    # Traversing a Linked List
    def listprint(self):
        curr = self.head
        res = []
        while curr.next != None:
            res.append(curr.val)
            curr = curr.next
        if curr.val:
            res.append(curr.val)

        print res


    # Inserting at the Beginning of the Linked List
    def insertBegin(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    # Inserting in between two Data Nodes
    def insertBetween(self, middleNode, val):
        if middleNode is None:
            return

        newNode = Node(val)
        newNode.next = middleNode.next
        middleNode.next = newNode

    # Removing an Item form a Liked List
    def removeNode(self, key):
        curr = self.head

        if curr.val:
            if curr.val == key:
                self.head = curr.next
                curr = None
                return

        while curr:
            if curr.val == key:
                break
            prev = curr
            curr = curr.next

        if curr is None:
            return

        prev.next = curr.next
        curr = None



link1 = Linklist()
link1.head = Node(1)
node2 = Node(2)
link1.head.next = node2
node3 = Node(3)
node4 = Node(4)

node2.next = node3
node3.next = node4



# Traversing a Linked List
link1.listprint()

print "-----------"

# Insertion in a Linked List
link1.insertBegin(0)
link1.listprint()

print "-----------"


# Inserting in between two Data Nodes
link1.insertBetween(link1.head.next, 100)
link1.listprint()

# Removing an Item form a Liked List

print "-----------"
link1.removeNode(3)
link1.listprint()