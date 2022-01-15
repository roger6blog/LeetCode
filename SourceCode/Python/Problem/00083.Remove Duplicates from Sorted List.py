'''
Level: Easy Tag:  LinkList


Given the head of a sorted linked list, delete all duplicates such that each element appears only once.

Return the linked list sorted as well.


Example 1:

"../../../Material/list1.jpeg"

Input: head = [1,1,2]
Output: [1,2]


Example 2:

"../../../Material/list2.jpeg"

Input: head = [1,1,2,3,3]
Output: [1,2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        seen = 0
        curr = head
        prev = None
        while curr:
            if curr.val == seen:
                break
            seen = curr.val
            prev = curr
            curr = curr.next

        prev.next = prev.next.next
        pass


head = [1,1,2,3,3]
link = list_to_link_list(head)
Solution().deleteDuplicates(link)
