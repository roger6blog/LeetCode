'''
Level: Medium   Tag: [Random]

A linked list of length n is given such that each node contains an additional random pointer,

which could point to any node in the list, or null.

Construct a deep copy of the list.

The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node.

Both the next and random pointer of the new nodes should point to new nodes in the copied list such that
the pointers in the original list and copied list represent the same list state.

None of the pointers in the new list should point to nodes in the original list.

For example,
if there are two nodes X and Y in the original list, where X.random --> Y,
then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.



Example 1:

"../../../Material/e1.png"

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:

"../../../Material/e2.png"

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:

"../../../Material/e3.png"

Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]


Constraints:

0 <= n <= 1000
-10^4 <= Node.val <= 10^4
Node.random is null or is pointing to some node in the linked list.

'''


'''
please see the problme 137 clone graph.
use the hash map/ dict to mapping the node: new node
Space: O(n)
'''


def list_to_link_list_random(head):
    for n in range(len(head))[::-1]:
        head[n] = Node(head[n][0], random=head[n][1])
        if n != len(head)-1:
            head[n].next = head[n+1]
    curr = head[0]
    n = len(head)
    while curr:
        if curr.random != None:
            curr.random = head[curr.random]
        curr = curr.next
        n += 1

    return head[0]

def link_list_to_list(head):
    ret = []
    while head.next:
        ret.append(head.val)
        head = head.next
    ret.append(head.val)
    return ret


# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return head

         #  mapping the node to new node
        hash_map = {}
        curr = head
        while curr:
            hash_map[curr] = Node(curr.val)
            curr = curr.next

        #  copy the next and ramdon pointer
        for node in hash_map:
            if node.next:
                hash_map[node].next = hash_map[node.next]
            if node.random:
                hash_map[node].random = hash_map[node.random]


        return hash_map[head]


head = [[7,None],[13,0],[11,4],[10,2],[1,0]]
link = list_to_link_list_random(head)
Solution().copyRandomList(link)