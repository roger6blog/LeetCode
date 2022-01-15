'''
Level: Medium   Tag:  LinkList

You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in reverse order and each of their nodes contain a single digit.

Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

"../../../Material/addtwonumber1.jpeg"

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

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
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def count_len(l):
            cnt = 1
            i = l
            num = l.val
            while i.next:

                i = i.next
                num += i.val * (10 ** cnt)
                cnt += 1

            return num

        t = None
        total_num = count_len(l1) + count_len(l2)
        for i in str(total_num)[::-1]:
            if not t:
                t = ListNode(i)
                ptr = t
            else:
                ptr.next = ListNode(i)
                ptr = ptr.next

        return t



a1 = ListNode(2)
a2 = ListNode(4)
a3 = ListNode(3)
a1.next = a2
a2.next = a3


b1 = ListNode(5)
b2 = ListNode(6)
b3 = ListNode(4)


b1.next = b2
b2.next = b3


sol = Solution()
sol.addTwoNumbers(a1, b1)









