

'''

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.

'''


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        ans = []
        for i in xrange(len(intervals)):
            if ans == []:
                ans.append(intervals[i])
            else:
                currlen = len(ans)
                if ans[currlen - 1].start <= intervals[i].start <= ans[currlen - 1].end:
                    ans[currlen - 1].end = max(ans[currlen - 1].end, intervals[i].end)
                else:
                    ans.append(intervals[i])
        return ans
        
        
   

d = Interval(15, 18)
b = Interval(2, 6)
c = Interval(8, 10)
a = Interval(1, 3)
sol = Solution()
lst = [a, b, c, d]
sol.merge(lst)
