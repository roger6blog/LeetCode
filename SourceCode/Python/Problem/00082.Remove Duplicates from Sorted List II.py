'''
Level: Medium  Tag:   [LinkList]

Given the head of a sorted linked list, delete all nodes that have duplicate numbers,

leaving only distinct numbers from the original list.

Return the linked list sorted as well.



Example 1:

"../../../Material/linkedlist1.jpeg"

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]


Example 2:

"../../../Material/linkedlist2.jpeg"

Input: head = [1,1,1,2,3]
Output: [2,3]


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

'''
删除链表中重复出现的节点，全部删掉一个都不保留

因为删除某个节点node，需要让node的前序节点.next = node.next，删除全部重复的元素可能删掉head元素
因此需要构造一个dummy node，让其指向head的前序节点，也就是dummy.next = head。
这样需要删除head的时候就可以令dummy.next = head.next。
最后反回dummy.next

'''


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        from collections import defaultdict
        def zero():
            return 0

        dup_map = defaultdict(zero)
        curr = head
        while curr:
            dup_map[curr.val] += 1
            curr = curr.next

        dummy = ListNode(None, head)
        curr = dummy
        while curr.next:
            if dup_map[curr.next.val] > 1:
                curr.next = curr.next.next
            else:
                curr = curr.next

        print(link_list_to_list(dummy.next))
        return dummy.next

head = [1,2,3,3,4,4,5]
link = list_to_link_list(head)
Solution().deleteDuplicates(link)