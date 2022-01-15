'''
Level: Medium  Tag: LinkList

Given the head of a singly linked list,

group all the nodes with odd indices together followed by the nodes with even indices,

and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.



Example 1:

"../../../Material/oddeven-linked-list.jpeg"

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:

"../../../Material/oddeven2-linked-list.jpeg"

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]


Constraints:

n == number of nodes in the linked list
0 <= n <= 104
-106 <= Node.val <= 106

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
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head


        odd_list = ListNode(1)
        even_list = ListNode(2)
        odd_curr = odd_list
        even_curr = even_list
        curr = head
        even = 1
        while curr:
            if even % 2 == 0:
                even_curr.next = curr
                even_curr = even_curr.next
            else:
                odd_curr.next = curr
                odd_curr = odd_curr.next
            curr = curr.next
            even += 1

        even_curr.next = None
        odd_curr.next = even_list.next

        return head






head = [1,2,3,4,5]
link = list_to_link_list(head)
link = Solution().oddEvenList(link)
print(link_list_to_list(link))