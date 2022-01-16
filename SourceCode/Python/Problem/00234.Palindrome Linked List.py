'''
Level: Easy  Tag:  LinkList

Given the head of a singly linked list, return true if it is a palindrome.


Example 1:


Input: head = [1,2,2,1]
Output: true

Example 2:


Input: head = [1,2]
Output: false


Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?


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

'''
純指針做法是用快慢指針來做
快指針走2步，慢指針每次走1步
當快指針走完時，慢指針必定走到中間
然後反轉後半部分
比較前半和後半部分是否相同
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head.next == None:
            return True

        palin = []

        curr = head
        while curr:
            palin.append(curr.val)
            curr = curr.next

        if len(palin) == 2:
            return palin[0] == palin[1]

        mid = len(palin) // 2
        if len(palin) % 2 == 0:
            left = mid - 1
            right = mid
        else:
            left = mid - 1
            right = mid + 1

        while left >= 0 and right < len(palin):
            if palin[left] != palin[right]:
                return False
            left -= 1
            right += 1

        return True


head = [1,2,2,1]
link = list_to_link_list(head)
assert True == Solution().isPalindrome(link)

head = [1,0,0]
link = list_to_link_list(head)
assert False == Solution().isPalindrome(link)

head = [1,0,1]
link = list_to_link_list(head)
assert True == Solution().isPalindrome(link)

head = [1,2]
link = list_to_link_list(head)
assert False == Solution().isPalindrome(link)

head = [1,2,2,2,1]
link = list_to_link_list(head)
assert True == Solution().isPalindrome(link)