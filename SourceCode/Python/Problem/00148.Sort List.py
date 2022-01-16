'''
Level: Medium    Tag: LinkList

Given the head of a linked list, return the list after sorting it in ascending order.


Example 1:

"../../../Material/sort_list_1.jpg"

Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:

"../../../Material/sort_list_2.jpg"

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]


Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is in the range [0, 5 * 10^4].
-10^5 <= Node.val <= 10^5


Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

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

'''
Quick sort的Linked list版本
'''

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def find_middle(head):
            if head == None or head.next == None:
                return head
            slow = head
            fast = head

            while fast and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def concat(left, middle, right):
            dummy = ListNode(None, left)
            curr = dummy
            while curr.next:
                curr = curr.next

            curr.next = middle
            while curr.next:
                curr = curr.next

            curr.next = right

            return dummy.next

        if head == None or head.next == None:
            return head

        pivot = find_middle(head)

        dummy_left = ListNode(None)
        dummy_mid = ListNode(None)
        dummy_right = ListNode(None)

        curr_left = dummy_left
        curr_mid = dummy_mid
        curr_right = dummy_right

        curr = head

        while curr:
            if curr.val > pivot.val:
                curr_right.next = curr
                curr_right = curr_right.next
            elif curr.val < pivot.val:
                curr_left.next = curr
                curr_left = curr_left.next
            else:
                curr_mid.next = curr
                curr_mid = curr_mid.next
            curr = curr.next

        curr_left.next = None
        curr_mid.next = None
        curr_right.next = None

        sorted_left = self.sortList(dummy_left.next)
        sorted_right = self.sortList(dummy_right.next)
        ans = concat(sorted_left, dummy_mid.next, sorted_right)
        print(link_list_to_list(ans))

        return ans



head = [-1,5,3,4,0]
link = list_to_link_list(head)
Solution().sortList(link)
