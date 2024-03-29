'''
Level : Easy   Tag: [LinkList]

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example1:

"../../../Material/rev1ex1.jpg"

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

"../../../Material/rev1ex2.jpg"

Input: head = [1,2]
Output: [2,1]


Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

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


"""
 null   [1,] -> [2,] -> [3,] -> [4,] -> [,5,]
  ↑       ↑
 prev   curr

1. 用temp记录下curr.next（因为后面要修改curr.next）
 null   [1,] -> [2,] -> [3,] -> [4,] -> [,5,]
  ↑       ↑      ↑
 prev   curr    temp

2. 将curr.next指向其前序节点prev，此时原来的后续链断掉:
 null <- [1,]  [2,] -> [3,] -> [4,] -> [,5,]
  ↑       ↑      ↑
 prev   curr    temp
3. 将prev移到curr位置，curr移动到原来的curr.next,即temp:
null <- [1,]  [2,] -> [3,] -> [4,] -> [,5,]
         ↑      ↑       ↑
        prev   curr    temp

"""


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr:
            next = curr.next   # 備份目前指向的箭頭                             next: 2->3->4->5  curr:1->2->3->4->5
            curr.next = prev   # 目前指向的下一個箭頭指到上一個點                curr: 1->None  prev: None
            prev = curr        # 把目前節點的值給存到應該之後成為上一個點的地方   prev: 1->None  curr:1->None
            curr = next        # 把備份指向的箭頭的點給目前的點                  curr: 2->3->4->5


        ans = prev
        return ans




head = [1,2,3,4,5]
link = list_to_link_list(head)
Solution().reverseList(link)