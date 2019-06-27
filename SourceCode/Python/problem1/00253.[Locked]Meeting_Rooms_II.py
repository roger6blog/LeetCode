
'''
Level: Hard Tag:[List]
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.

'''
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def minMeetingRooms(self, intervals):
        if intervals == [] or len(intervals) == 0:
            return 0

        tmp = []

        for i in intervals:
            tmp.append([i.start, True])
            tmp.append([i.end, False])

        tmp.sort(key=lambda x: x[0])

        maxNum = 0
        currNum = 0

        for node, isStart in tmp:
            if isStart:
                currNum += 1
            else:
                currNum -= 1
            maxNum = max(maxNum, currNum)
        return maxNum

    
a = Interval(0, 30)
b = Interval(5, 10)
c = Interval(15, 20)
s = [a,b,c]
sol = Solution()
print sol.minMeetingRooms(s)
        
        
