'''
Level: Easy  Tag:  LinkList

Given the head of a linked list and an integer val,

remove all the nodes of the linked list that has Node.val == val,

and return the new head.


Example 1:

"../../../Material/removelinked-list.jpg"

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]


Example 2:

Input: head = [], val = 1
Output: []

Example 3:

Input: head = [7,7,7,7], val = 7
Output: []


Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50

'''

def list_to_link_list(head):
    for n in range(len(head))[::-1]:
        head[n] = ListNode(head[n])
        if n != len(head)-1:
            head[n].next = head[n+1]

    return head[0]

def link_list_to_list(head):
    ret = []
    while head.next:
        ret.append(head.val)
        head = head.next
    ret.append(head.val)
    return ret


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(None, head)
        curr = dummy
        while curr.next:
            if curr.next.val == val:
                    curr.next = curr.next.next
            else:
                curr = curr.next


        print(link_list_to_list(dummy))
        return dummy.next

head = [1,2,6,3,4,5,6]
val = 6
link = list_to_link_list(head)
Solution().removeElements(link, val)


head = [7,7,7,7]
val = 7
link = list_to_link_list(head)
Solution().removeElements(link, val)