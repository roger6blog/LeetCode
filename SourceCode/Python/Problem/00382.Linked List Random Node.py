'''
Level: Medium   Tag: [Random]

Given a singly linked list,

return a random node's value from the linked list.

Each node must have the same probability of being chosen.

Implement the Solution class:

Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
int getRandom() Chooses a node randomly from the list and returns its value.
All the nodes of the list should be equally likely to be chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you?
Could you solve this efficiently without using extra space?



Example:

"../../../Material/getrand-linked-list.jpeg"

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly.
Each element should have equal probability of returning.
solution.getRandom();


'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
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

        print(res)


    # Inserting at the Beginning of the Linked List
    def insertBegin(self, val):
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode

    # Inserting in between two Data Nodes
    def insertBetween(self, middleNode, val):
        if middleNode is None:
            return

        newNode = ListNode(val)
        newNode.next = middleNode.next
        middleNode.next = newNode

    # Removing an Item form a Liked List
    def removeNode(self, key):
        curr = self.head
        prev = None
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

        if prev:
            prev.next = curr.next
        curr = None

import random
class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.length = 0
        while head:
            self.length += 1
            head = head.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        index = random.randint(0, self.length - 1)
        count = 0
        ptr = self.head
        while ptr:
            if count == index:
                return ptr.val
            count += 1
            ptr = ptr.next

'''
水塘取樣演算法
在未知長度的樣本中用同等的機率取出樣本
'''


class Solution_follow_up(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        ans = None
        count = 0
        ptr = self.head
        while ptr:
            count += 1
            x = random.randint(1, count)
            if x == 1:
                ans = ptr.val
            ptr = ptr.next

        return ans

link1 = Linklist()
link1.head = ListNode(1)
node2 = ListNode(2)
link1.head.next = node2
node3 = ListNode(3)
node4 = ListNode(4)

node2.next = node3
node3.next = node4
link1.listprint()
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

