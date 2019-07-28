'''
1124. Longest Well-Performing Interval

Medium

We are given hours, a list of the number of hours worked per day for a given employee.

A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.



Example 1:

Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].


Constraints:

1 <= hours.length <= 10000
0 <= hours[i] <= 16

'''


class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        begin = 0
        ans = 0
        for c, h in enumerate(hours):
            if h <= 8:
                begin += 1

            ans = max(ans, len(hours[begin:c]))
        return ans


hours = [9,9,6,0,6,6,9]
hours2 = [6,6,6]
sol = Solution().longestWPI(hours)