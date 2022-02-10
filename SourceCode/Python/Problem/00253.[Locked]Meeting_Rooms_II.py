
'''
Level: Hard (2021 changed to Medium) Tag:[List][Sweep Line]

Given an array of meeting time intervals consisting of
start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)

Example2

Input: intervals = [(2,7)]
Output: 1
Explanation:
Only need one meeting room

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


    # 扫描线，按时间从小到大排序，若是起点，count++，若是终点，count--
    def minMeetingRooms_sweep_line(self, intervals):
        rooms = []
        start = 0
        end = 1
        for i in intervals:
            rooms.append((i[start], 1))
            rooms.append((i[end], -1))

        rooms.sort(key=lambda x: x[start])
        ans = 0
        tmp = 0
        for _, cost in rooms:
            tmp += cost
            ans = max(ans, tmp)

        return ans




a = Interval(0, 30)
b = Interval(5, 10)
c = Interval(15, 20)
s = [a,b,c]
sol = Solution()
print(sol.minMeetingRooms(s))

s = [[0, 30],[5, 10],[15, 20]]
print(sol.minMeetingRooms_sweep_line(s))

