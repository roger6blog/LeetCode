'''
Level: Easy

A binary watch has 4 LEDs on the top which represent the hours (0-11),

and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.

(https://upload.wikimedia.org/wikipedia/commons/8/8b/Binary_clock_samui_moon.jpg)

For example, the above binary watch reads "4:51".

"../../../Material/binarywatch.jpg"

Given an integer turnedOn which represents the number of LEDs that are currently on,

return all possible times the watch could represent. You may return the answer in any order.

The hour must not contain a leading zero.


Example:

Input: turnedOn = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

Example 2:

Input: turnedOn = 9
Output: []


Constraints:

0 <= turnedOn <= 10

Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid,
it should be "10:02".


'''

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """

        ans = []
        for h in xrange(12):
            for m in xrange(60):
                if (bin(m) + bin(h)).count('1') == num:
                    # print "{:d}:{:02d}".format(h, m)
                    ans.append("{:d}:{:02d}".format(h, m))
        return ans
n = 4
print(Solution().readBinaryWatch(n))