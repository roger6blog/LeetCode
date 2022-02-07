'''
Level: Medium

Given a time represented in the format "HH:MM",

form the next closest time by reusing the current digits.

There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example,

"01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39,
which occurs 5 minutes later.
It is not 19:33, because this occurs 23 hours and 59 minutes later.

Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.


'''


class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        digits = set(time)
        while True:
            time = self.nextTime(time)
            # It's equal to set(time).issubset(digits)
            if set(time) <= digits:
                break
        return time


    def nextTime(self, time):
        hour, minute = map(int, time.split(":"))
        carryFlag = (minute + 1) // 60
        minute = (minute + 1) % 60
        hour = (hour + carryFlag) % 24
        return "{:2d}:{:2d}".format(hour, minute)






    def nextClosestTime2(self, time):
        """
        :type time: str
        :rtype: str
        """
        h, m = map(int, time.split(":"))
        curr = h * 60 + m
        for c in range(curr+1, 1441):
            h = c // 60
            m = c % 60
            next_time = "{:02d}:{:02d}".format(h, m)
            if set(next_time) <= set(time):
                return next_time


clock  = "19:34"
print(Solution().nextClosestTime2(clock))
clock2 = "23:59"
print(Solution().nextClosestTime(clock2))