'''

1167. Minimum Cost to Connect Sticks

Difficulty: Medium
You have some sticks with positive integer lengths.

You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.  You perform this action until there is one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.



Example 1:

Input: sticks = [2,4,3]
Output: 14
Example 2:

Input: sticks = [1,8,3,5]
Output: 30


Constraints:

1 <= sticks.length <= 10^4
1 <= sticks[i] <= 10^4

'''
import heapq
class Solution(object):
    def __init__(self):
        self.sticks = None
        self.curr = 0
        self.ans = 0
    def merge(self):
        min_1 = heapq.heappop(self.sticks)
        min_2 = heapq.heappop(self.sticks)
        new_stick = min_1 + min_2
        heapq.heappush(self.sticks, new_stick)
        if len(self.sticks) > 1:
            self.curr += new_stick
            self.merge()
        else:
            self.ans =  self.curr + self.sticks[0]
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        self.sticks = sticks
        heapq.heapify(self.sticks)
        self.merge()
        return self.ans


#sticks = [2,4,3]
sticks = [1,8,3,5]
#sticks = [3354,4316,3259,4904,4598,474,3166,6322,8080,9009]
Solution().connectSticks(sticks)