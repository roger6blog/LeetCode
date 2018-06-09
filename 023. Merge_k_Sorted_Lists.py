

'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# For unit test Start
import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def add(self, data):
        newNode = ListNode(data)

        newNode.next = self.next
        self.next = newNode
# For unit test End

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        heap = []
        for node in lists:
            if node:
                heap.append((node.val, node))
        heapq.heapify(heap)
        head = ListNode(0)
        curr = head

        while heap:
            pop = heapq.heappop(heap)
            curr.next = ListNode(pop[0])
            curr = curr.next
            if pop[1].next:
                heapq.heappush(heap, (pop[1].next.val, pop[1].next))

        return head.next
        
        
  # Test program
  
lst = ListNode(1)

lst.add(4)
lst.add(5)
print lst
lst2 = ListNode(1)
lst2.add(3)
lst2.add(4)
lst3 = ListNode(2)
lst2.add(6)

lists = []
lists.append(lst)
lists.append(lst2)
lists.append(lst3)
#lists = [[1,4,5],[1,3,4],[2,6]]
a =  mergeKLists(lists)
print a
