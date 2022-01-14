'''
Level : Easy   Tag: LinkList

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example1:

"../../../Material/rev1ex1.jpg"

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

"../../../Material/rev1ex2.jpg"

Input: head = [1,2]
Output: [2,1]


Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

'''

def init_link_list(head):
    for n in range(len(head))[::-1]:
        head[n] = ListNode(head[n])
        if n != len(head)-1:
            head[n].next = head[n+1]

    return head[0]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next


        ans = prev
        return ans




head = [1,2,3,4,5]
link = init_link_list(head)
Solution().reverseList(link)