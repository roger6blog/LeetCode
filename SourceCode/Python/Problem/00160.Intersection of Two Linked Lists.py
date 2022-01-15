'''
Level: Easy   Tag:  LinkList

Given the heads of two singly linked-lists headA and headB,

return the node at which the two lists intersect.

If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:

"../../../Material/160_statement.png"

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs.
This is 0 if there is no intersected node.

listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads,
headA and headB to your program.
If you correctly return the intersected node, then your solution will be accepted.


Example 1:

"../../../Material/160_example_1_1.png"


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5].
There are 2 nodes before the intersected node in A;
There are 3 nodes before the intersected node in B.

Example 2:

"../../../Material/160_example_2.png"

Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4].
There are 3 nodes before the intersected node in A;
There are 1 node before the intersected node in B.

Example 3:

"../../../Material/160_example_3.png"

Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. S
ince the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.


Constraints:

The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
1 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA < m
0 <= skipB < n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.


Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?

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


'''
設計一個while迴圈，只有在a==b的時候才離開 意思就是兩這個intersection
迴圈裡a和b一直走到底，誰先走到底了就換到對面的linkedlist繼續走
當第一次迭代有人先走到底跳到對面時，a和b的差距就是兩個linkedlist的長度之差
當另一個走比較長linkedlist的人走到底，跳到比較短的linkedlist時
這兩者必定會在intersection點相遇
如果沒有intersection的時候，他們就會一起走到底
'''


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        a = headA
        b = headB
        while a != b:
            if a == None:
                a = headB
            else:
                a = a.next

            if b == None:
                b = headA
            else:
                b = b.next

        return a




