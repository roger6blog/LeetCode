'''
## Meeting Rooms I, II

>**Question 1**

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...] (si < ei)`, determine if a person could attend all meetings.

For example,

Given `[[0, 30],[5, 10],[15, 20]]`,  
return false.

>**Solution**

The idea is pretty simple: first we sort the intervals in the ascending order of start; then we check for the overlapping of each pair of neighboring intervals. If they do, then return false; after we finish all the checks and have not returned false, just return true.

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
        for i in xrange(len(timeLst)-1):
            if timeLst[i+1].start < timeLst[i].end:
                return False

        return True
        
        
s1 = Interval(0, 30)
s2 = Interval(5, 10)
s3 = Interval(15, 20)
sol = Solution()
a = sol.isAbleAttend([s1, s3, s3])
print a       
