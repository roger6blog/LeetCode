'''
Level: Medium   Tag:  LinkList

Given a non-negative integer represented as non-empty a singly linked list of digits,

plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.



Example1

Input: 1 -> 2 -> 3 -> null
Output: 1 -> 2 -> 4 -> null
Explanation:
123 + 1 = 124

Example2

Input: 9 -> 9 -> null
Output: 1 -> 0 -> 0 -> null
Explanation:
99 + 1 = 100


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


#Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
'''
先反轉一次 然後第一個node加一
之後就判斷是否有進位決定後面的節點是否加一
如果最後的節點還有近位那就要多加一個1的節點上去
最後再反轉一次這個linkedlist即為所求

'''

class Solution:
    """
    @param head: the first Node
    @return: the answer after plus one
    """
    def plusOne(self, head):
        # Write your code here

        curr = head
        rev_list = None
        while curr:
            next = curr.next
            curr.next = rev_list
            rev_list = curr
            curr = next

        carry = False
        curr = rev_list
        carry = False
        curr.val = (curr.val+1) % 10
        if curr.val == 0:
            carry = True

        curr = curr.next
        prev = None
        while curr:
            if carry == True:
                curr.val = (curr.val+1) % 10
            if curr.val == 0:
                carry = True
            else:
                carry = False

            prev = curr
            curr = curr.next

        if carry == True:
            prev.next = ListNode(1)

        curr = rev_list
        head = None
        while curr:
            next = curr.next
            curr.next = head
            head = curr
            curr = next

        print(link_list_to_list(head))
        return head

head = [1, 2, 3]
link = list_to_link_list(head)
Solution().plusOne(link)


head = [9, 9]
link = list_to_link_list(head)
Solution().plusOne(link)
