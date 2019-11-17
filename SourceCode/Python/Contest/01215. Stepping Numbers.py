'''

5081->1215. Stepping Numbers
Difficulty: Medium
A Stepping Number is an integer such that all of its adjacent digits have an absolute difference of exactly 1.

For example, 321 is a Stepping Number while 421 is not.

Given two integers low and high,

find and return a sorted list of all the Stepping Numbers in the range [low, high] inclusive.



Example 1:

Input: low = 0, high = 21
Output: [0,1,2,3,4,5,6,7,8,9,10,12,21]


Constraints:

0 <= low <= high <= 2 * 10^9


'''
from collections import deque
class Solution(object):
    def countSteppingNumbers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """


        ans = []
        def bfs(n, m, i):
            qq = deque()
            qq.append(i)

            while len(qq) > 0:
                s = qq.pop()
                if s <= m and s >= n:
                    ans.append(s)

                if i == 0 or s > m:
                    continue

                last = s % 10
                s1 = s * 10 + (last - 1)
                s2 = s * 10 + (last + 1)

                if last == 0:
                    qq.append(s2)
                elif last == 9:
                    qq.append(s1)
                else:
                    qq.append(s1)
                    qq.append(s2)

        for i in range(10):
            bfs(low, high, i)

        return sorted(ans)
