
'''
LeveL: Hard (2021 change to Medium)  Tag: [List]

Given a set of non-overlapping intervals,
insert a new interval into the intervals
(merge if necessary).

You may assume that the intervals were initially sorted according to their start times.


====   2021 new description   ====

You are given an array of non-overlapping intervals intervals where
intervals[i] = [start(i), end(i)] represent the start and the end of the i(th) interval and
intervals is sorted in ascending order by starti.

You are also given an interval newInterval = [start, end] that
represents the start and end of another interval.

Insert newInterval into intervals such that
intervals is still sorted in ascending order by start(i) and intervals still does not have
any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

====   2021 new description   ====

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by start(i) in ascending order.
newInterval.length == 2
0 <= start <= end <= 105

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
        for i in range(len(intervals)):
            if ans == []:
                ans.append(intervals[i])
            else:
                if ans[-1].start <= intervals[i].start <= ans[-1].end:
                    ans[-1].end = max(ans[-1].end, intervals[i].end)

                else:
                    ans.append(intervals[i])

        return ans


    def insert_no_class(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        start = 0
        end = 1

        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[start])
        ans = []
        for interval in intervals:
            if ans == []:
                ans.append(interval)
                continue

            if ans[-1][end] < interval[start]:
                ans.append(interval)

            else:
                ans[-1][end] = max(ans[-1][end], interval[start])

            ans[-1][end] = max(ans[-1][end], interval[end])

        return ans



a = [Interval(1,3),Interval(6,9)]
b = Interval(2,5)
sol = Solution()
print(sol.insert(a, b))
a = [[1,3], [6,9]]
b = [2,5]
print(Solution().insert_no_class(a, b))
a = [[1,5]]
b = [2,7]
expect = [[1,7]]


