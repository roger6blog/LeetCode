'''
Level: Medium  Tag:  LinkList

Given the head of a linked list,

remove the n'th node from the end of the list and return its head.


Example 1:

"../../../Material/remove_ex1.jpeg"


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


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



'''
快慢指針
先讓快的指針走n步
然後大家同時每次走一步
快指針走到結尾的時候
慢指針指的節點即為要刪除的節點
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next == None:
            return head.next

        dummy = ListNode(0, head)
        fast = head
        slow = dummy
        for _ in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next


# head = [1,2,3,4,5]
# n = 2
# link = list_to_link_list(head)
# Solution().removeNthFromEnd(link, n)

head = [1,2]
n = 1
link = list_to_link_list(head)
Solution().removeNthFromEnd(link, n)

head = [1,2,3]
n = 3
link = list_to_link_list(head)
Solution().removeNthFromEnd(link, n)