'''
Level: Medium  Tag:  LinkList

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln-1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.


Example 1:

"../../../Material/reorder1linked-list.jpg"

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:

"../../../Material/reorder2-linked-list.jpg"

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]


Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000


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
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        mid = head
        fast = head

        # 依序輪流檢查
        while fast and fast.next and fast.next.next:
            mid = mid.next
            fast = fast.next.next


        curr = mid.next
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        mid.next = None             # 要斷開3->4的這段連結。沒做這步 會形成cicrular list
                                    # prev = 4, mid = 3
        curr = head                 # curr = 1->2->3->4
        while prev:
            next = prev.next        # next = None
            prev.next = curr.next   # prev = 4->2->3
            curr.next = prev        # curr = 1->4->2->3
            curr = curr.next.next   # curr = 2->3
            prev = next             # prev = 3

        print(link_list_to_list(head))
        return head


head = [1,2,3,4]
link = list_to_link_list(head)
Solution().reorderList(link)


head = [1,2,3,4,5]
link = list_to_link_list(head)
Solution().reorderList(link)