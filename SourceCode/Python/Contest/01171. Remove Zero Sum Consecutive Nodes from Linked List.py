'''

1171. Remove Zero Sum Consecutive Nodes from Linked List

Difficulty: Medium
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.



(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]


Constraints:

The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.lst = []
        self.ans = None
        def remove_abs(value):
            removed = False
            if not self.lst:
                self.lst.append(value)
            elif self.lst[-1] != (value * -1):
                self.lst.append(value)
            else:
                del self.lst[-1]
                removed = True

            return removed

        def rec_remove(lst):
            is_remove = False
            for c, i in enumerate(lst):
                if remove_abs(i):
                    is_remove = True

            if is_remove:
                self.lst = []
                rec_remove(lst)

            else:
                self.ans = lst
        ptr = head
        lst = []
        while ptr.next != None:
            lst.append(ptr.val)
            ptr = ptr.next
        else:
            lst.append(ptr.val)
        rec_remove(lst)


        return lst



head = [1,2,3,-3,4]
lst1 = ListNode(1)
lst2 = ListNode(2)
lst3 = ListNode(3)
lst4 = ListNode(-3)
lst5 = ListNode(4)
lst1.next = lst2
lst2.next = lst3
lst3.next = lst4
lst4.next = lst5

print(Solution().removeZeroSumSublists(lst1))