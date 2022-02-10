'''
Level:  Medium  Tag: [PreSum] [Slide Window]

There are several cards arranged in a row, and each card has an associated number of points.

The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row.
You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.



Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However,
choosing the rightmost card first will maximize your total score.
The optimal strategy is to take the three cards on the right,
giving a final score of 1 + 6 + 5 = 12.

Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.


Constraints:

1 <= cardPoints.length <= 10^5
1 <= cardPoints[i] <= 10^4
1 <= k <= cardPoints.length

'''

class Solution(object):
    '''
    题目等价于：求从 cardPoints 最左边抽 i 个数字，从 cardPoints 最右边抽取 k - i 个数字，能抽取获得的最大点数是多少。
    所以：抽走的卡牌点数之和 = cardPoints 所有元素之和 - 剩余的中间部分元素之和。
    所有元素之和是固定的，所以目標就是中間元素之和為最小
    中間元素之和可以用presum來求 i ~ j 區間的和

    "../../../Material/20210206195627684.gif"

    '''
    def maxScore_pre_sum(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        if k >= len(cardPoints):
            return sum(cardPoints)
        ans = float('inf')
        n = len(cardPoints)
        pre_sum = [0] * (n+1)
        for i in range(n):
            pre_sum[i+1] = pre_sum[i] + cardPoints[i]

        window_size= n - k
        for i in range(k+1):
            # 此即為i~j的區間和:
            # 0 ~ n-k 的區間和 減去到 0 ~ i 元素的區間和 = i ~ n-k 的區間和
            ans = min(ans, pre_sum[window_size+i] - pre_sum[i])


        ans = pre_sum[n] - ans
        print(ans)
        return ans

    def maxScore_deque(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        from collections import deque
        queue = deque()
        n = len(cardPoints)
        ans = float('inf')
        for i in cardPoints:
            queue.append(i)
            while len(queue) > n-k:
                queue.popleft()

            if len(queue) == n-k:
                ans = min(ans, sum(queue))

        ans = sum(cardPoints) - ans
        print(ans)

        return ans

    def maxScore_slide(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """

        n = len(cardPoints)
        ans = float('inf')
        window_size = n - k
        sums = 0
        for i in range(n):
            sums += cardPoints[i]

            # 当 i >= windowSize 时，为了固定窗口的元素是 k 个，每次移动时需要将 i - windowSize 位置的元素移除
            if i >= window_size:
                sums -= cardPoints[i-window_size]
            # 当 i >= windowSize - 1 时，滑动窗口内的元素刚好是 k 个，开始计算滑动窗口的最小和。
            if i >= window_size-1:
                ans = min(ans, sums)

        ans = sum(cardPoints) - ans
        print(ans)

        return ans


cardPoints = [1,2,3,4,5,6,1]
k = 3
Solution().maxScore_slide(cardPoints, k)