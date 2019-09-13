'''
5183->1185. Day of the Week
Difficulty: Easy
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

'''
import datetime
class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        dic_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        today = datetime.datetime(year, month, day, 0, 0 ,0)
        weekday = today.weekday()
        return dic_week[weekday]



day = 31
month = 8
year = 2019
print(Solution().dayOfTheWeek(day, month, year))