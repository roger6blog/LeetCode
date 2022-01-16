'''
Level: Medium   Tag: LinkList

Given the head of a linked list and a value x,

partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.



Example 1:

"../../../Material/partition.jpg"

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]


Example 2:

Input: head = [2,1], x = 2
Output: [1,2]


Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200


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
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        dummy_left = ListNode(-1)
        dummy_right = ListNode(-1)

        curr_left = dummy_left

        curr_right = dummy_right

        curr = head

        while curr:
            if curr.val >= x:
                curr_right.next = curr
                curr_right = curr_right.next
            elif curr.val < x:
                curr_left.next = curr
                curr_left = curr_left.next
            curr = curr.next

        curr_left.next = None
        curr_right.next = None

        dummy = ListNode(-1, dummy_left.next)
        curr = dummy
        while curr.next:
            curr = curr.next

        curr.next = dummy_right.next


        print(link_list_to_list(dummy.next))

        return dummy.next



head = [1,4,3,2,5,2]
x = 3
link = list_to_link_list(head)
Solution().partition(link, x)