'''
Level: Medium  Tag: [Math]

You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order.

Apply the following algorithm on arr:

Starting from left to right, remove the first number and every other number afterward until
you reach the end of the list.
Repeat the previous step again, but this time from right to left,
remove the rightmost number and every other number from the remaining numbers.
Keep repeating the steps again, alternating left to right and right to left, until a single number remains.
Given the integer n, return the last number that remains in arr.


Example 1:

Input: n = 9
Output: 6
Explanation:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [2, 4, 6, 8]
arr = [2, 6]
arr = [6]

Example 2:

Input: n = 1
Output: 1


Constraints:

1 <= n <= 10^9



[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
[2, 6, 10, 14, 18]
[6, 14]
[6]

我們首先分析能夠得到的信息。一個很容易觀察到的變化規律就是步長信息，那我們就首先得到步長的規律。
觀察第一列的步長爲2，第二列的步長爲4（相隔元素），
第三列元素爲8（假設存在10 11 12 第二列元素就變成 2 4 6 8 10 12 第三列就變成 2 6 10），
也就是說步數在每輪循環中是上一輪的兩倍。我們再來觀察元素個數遞減規律，發現元素個數是按1/2的速度遞減的。
當遞減元素個數減少到1時，就得到了最終的剩餘元素。
最難的部分就是追蹤每次的頭部元素，很容易觀察到的一個結論是，從左側開始的頭部元素都是上一次的頭部元素加上步長。
對於從右側開始的迭代過程，則分爲兩種情況，一種情況是左側頭部元素不變，
一種情況是左側頭部元素爲上次迭代的頭部元素加步長，
對於後一種情況，我們容易觀察到的一點是，在剩餘元素是奇數個時，頭部元素會發生改變，否則不變

'''

class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        is_left = True
        head = 1
        step = 1
        remain = n
        while remain > 1:
            if is_left or remain % 2 == 1:
                head += step
            print(head)
            step *= 2
            remain /= 2
            is_left = not is_left

        # print(head)

        return head


n = 9
Solution().lastRemaining(n)

n = 20
Solution().lastRemaining(n)