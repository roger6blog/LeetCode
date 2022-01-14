'''
Level: Medium  Tag: LinkList

Given a linked list, swap every two adjacent nodes and return its head.

You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)


Example 1:

"../../../Material/swap_ex1.jpg"

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]


Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100


'''






'''

非遞回寫法:
原本list:  prev->1->2->3->4->dummy
新list:  dummy->2->1->4->3->None
操作步驟
"../../../Material/swap-step1.png"
操作結果
"../../../Material/swap-step2.png"
拉成linked list來看
"../../../Material/swap-summary.png"
'''

def init_link_list(head):
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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0, head)       # prev = 0->1->2->3->4
        curr = dummy
        while curr.next and curr.next.next:

            orig = curr.next
            stash = curr.next.next.next   # stash = 3->4

            # "../../../Material/swap-step1.png"

            curr.next = curr.next.next    # step1, curr = 0->2->3->4
            curr.next.next = orig         # step2, curr = 0->2->1->2..(circular)
            curr.next.next.next = stash   # step3, curr = 0->2->1->3->4

            curr = curr.next.next

        return dummy.next

head = [1,2,3,4]
link = init_link_list(head)
print(link_list_to_list(link))
link = Solution().swapPairs(link)
print(link_list_to_list(link))