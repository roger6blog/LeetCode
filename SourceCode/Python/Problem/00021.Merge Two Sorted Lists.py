'''
Level: Easy  Tag:  LinkList

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list.

The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


Example 1:

"../../../Material/merge_ex1.jpeg"

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.



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
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(None)
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next


        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        print(link_list_to_list(dummy.next))
        return dummy.next

list1 = [1,2,4]
list2 = [1,3,4]
link1 = list_to_link_list(list1)
link2 = list_to_link_list(list2)
Solution().mergeTwoLists(link1, link2)