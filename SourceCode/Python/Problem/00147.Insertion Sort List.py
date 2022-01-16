'''
Level: Medium   Tag: LinkList

Given the head of a singly linked list,

sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list.

One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

"../../../Material/Insertion-sort-example-300px.gif"


Example 1:

"../../../Material/sort1linked-list.jpg"

Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:

"../../../Material/sort2linked-list.jpg"

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]


Constraints:

The number of nodes in the list is in the range [1, 5000].
-5000 <= Node.val <= 5000


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
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0)
        curr = head

        while curr:
            curr_dummy = dummy.next
            pre_curr_dummy = dummy
            # 尋找插入點，如果是空串列，直接插入
            # 否則找到新串列中值比未排序串列節點值大的節點處
            while curr_dummy and curr_dummy.val < curr.val:
                pre_curr_dummy = curr_dummy
                curr_dummy = curr_dummy.next

            # 在新串列的較大節點處之前  插入未排序串列的節點
            post = curr.next               # 保留未排序串列的連結             post = 2->1->3
            pre_curr_dummy.next = curr     # 插入要插入的未排序串列到馨串列中  pre_curr_dummy = 0->4->2->1->3
            curr.next = curr_dummy         # 斷開插入節點和舊串列的連結       curr = 4, pre_curr_dummy = 0->4
            curr = post                    # 恢復未排序串列的連結             curr = 2->1->3

        print(link_list_to_list(dummy.next))

        return dummy.next


head = [4,2,1,3]
link = list_to_link_list(head)
Solution().insertionSortList(link)