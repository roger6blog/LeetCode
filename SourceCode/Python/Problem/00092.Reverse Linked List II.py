'''
Level: Medium Tag: LinkList


Given the head of a singly linked list and two integers left and right where left <= right,

reverse the nodes of the list from position left to position right, and return the reversed list.



Example 1:

"../../../Material/rev2ex2.jpeg"

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]


Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n


Follow up: Could you do it in one pass?



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
一直记录换完区间的头，让reverse区间之前的node的next等于reverse区间的头
'''

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == right:
            return head

        dummy = ListNode(0, head)
        rev_list = dummy
        for _ in range(left-1):
            rev_list = rev_list.next
        curr = rev_list.next          # curr = 2->3->4->5, rev_list = 1->2->3->4->5
        '''
        總共算2次
        0. 2->3-4
        1. 3->2->4
        2. 4->3->2
        '''
        for _ in range(right-left):
            next = curr.next          # next = 3->4->5
            curr.next = next.next     # curr = 2->4->5, rev_list = 1->2->4->5
            next.next = rev_list.next # next = 3->2->4->5
            rev_list.next = next      # rev_list = 1->3->2->4->5

        return dummy.next


    '''
    準備prefix為起點
    postfix為終點
    反轉中間擷取的linkedlist
    最後把prefix->反轉的linkedlist->postfix串起來即為所求
    但是某些case不能pass
    '''
    def reverseBetween_wrong_ans(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == right:
            return head
        curr = head
        count = 2
        prefix = ListNode(0, head)
        while count <= left:
            curr = curr.next
            count += 1
            prefix = prefix.next

        rev_list = curr
        rev_curr = rev_list
        while count <= right:
            curr = curr.next
            rev_curr = rev_curr.next
            count += 1

        postfix = rev_curr.next
        rev_curr.next = None

        curr = rev_list
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        curr = prev
        while curr.next:
            curr = curr.next

        curr.next = postfix
        prefix.next = prev
        if prefix.val == 0:
            return prefix.next
        return prefix


head = [1,2,3,4,5]
left = 2
right = 4
link = list_to_link_list(head)
link = Solution().reverseBetween(link, left, right)
print(link_list_to_list(link))
assert [1, 4, 3, 2, 5] == link_list_to_list(link)


head = [3, 5]
left = 1
right = 2
link = list_to_link_list(head)
link = Solution().reverseBetween(link, left, right)
print(link_list_to_list(link))

head = [1,2,3,4,5]
left = 3
right = 4
link = list_to_link_list(head)
link = Solution().reverseBetween(link, left, right)
print(link_list_to_list(link))