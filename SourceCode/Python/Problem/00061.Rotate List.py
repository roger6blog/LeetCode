'''
Level: Medium   Tag: LinkList

Given the head of a linked list, rotate the list to the right by k places.


Example 1:

"../../../Material/rotate1.jpg"

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

"../../../Material/roate2.jpg"

Input: head = [0,1,2], k = 4
Output: [2,0,1]


Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 10^9

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
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        def rorate(head):
            curr = head

            while curr.next:
                prev = curr
                curr = curr.next

            prev.next = None
            rorate = curr
            rorate.next = head
            return rorate

        if k == 0 or head == None or head.next == None:
            return head
        head_len = 0
        curr = head
        while curr:
            head_len += 1
            curr = curr.next

        k = k % head_len

        for _ in range(k):
            head = rorate(head)

        print(link_list_to_list(head))
        return head


head = [1,2,3,4,5]
k = 2
link = list_to_link_list(head)
Solution().rotateRight(link, k)

head = [0,1,2]
k = 4
link = list_to_link_list(head)
Solution().rotateRight(link, k)


head = [1,2,3]
k = 2000000000
link = list_to_link_list(head)
Solution().rotateRight(link, k)

head = []
k = 0
link = list_to_link_list(head)
Solution().rotateRight(link, k)
