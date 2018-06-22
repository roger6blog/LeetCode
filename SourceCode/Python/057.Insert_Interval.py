
'''
LeveL: Hard   Tag: [List]

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

'''


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x.start)
        ans = []
        for i in xrange(len(intervals)):
            if ans == []:
                ans.append(intervals[i])
            else:
                if ans[-1].start <= intervals[i].start <= ans[-1].end:
                    ans[-1].end = max(ans[-1].end, intervals[i].end)

                else:
                    ans.append(intervals[i])

        return ans
                                 

a = [Interval(1,3),Interval(6,9)]
b = Interval(2,5)
sol = Solution()
print sol.insert(a, b)
