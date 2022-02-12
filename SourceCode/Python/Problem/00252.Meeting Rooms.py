'''
Level: Easy  Tag: [Sweep Line]

## Meeting Rooms I

>**Question 1**

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...] (si < ei)`,

determine if a person could attend all meetings.

For example,

Given `[[0, 30],[5, 10],[15, 20]]`,
return false.
Explanation:
(0,30), (5,10) and (0,30),(15,20) will conflict

Example2

Input: intervals = [(5,8),(9,15)]
Output: true
Explanation:
Two times will not conflict

>**Solution**

The idea is pretty simple: first we sort the intervals in the ascending order of start;

then we check for the overlapping of each pair of neighboring intervals. If they do, then return false;

after we finish all the checks and have not returned false, just return true.

Sorting takes O(nlogn) time and the overlapping checks take O(n) time, so this idea is O(nlogn) time in total.

'''



# Definition for an interval.
class Interval:
    def __init__(self, si, ei):
        self.start = si
        self.end = ei


class Solution(object):
    def isAbleAttend(self, timeLst):
        timeLst.sort(key=lambda x: x.start)
        for i in range(len(timeLst)-1):
            if timeLst[i+1].start < timeLst[i].end:
                return False

        return True


    def isAbleAttend_no_class(self, timeLst):
        start = 0
        end = 1
        timeLst.sort(key=lambda x: x[start])
        for i in range(len(timeLst)-1):
            if timeLst[i][end] > timeLst[i+1][start]:
                return False

        return True



    def isAbleAttend_overlap(self, timeLst):
        def overlap(a, b):
            if min(0, max(a[0], b[0] - min(a[1], b[1]))) > 0:
                return True

            return False


        timeLst.sort()
        for i in range(len(timeLst)-1):
            if overlap(timeLst[i], timeLst[i+1]):
                retunr False

        return True


s1 = Interval(0, 30)
s2 = Interval(5, 10)
s3 = Interval(15, 20)
sol = Solution()
a = sol.isAbleAttend([s1, s3, s3])
print(a)

meetings = [[0, 30],[5, 10],[15, 20]]
print(Solution().isAbleAttend_no_class(meetings))
print(Solution().isAbleAttend_overlap(meetings))
