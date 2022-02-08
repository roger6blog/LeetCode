'''
Level: Medium  Tag: [Sweep Line]

You are implementing a program to use as your calendar.

We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection
(i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open
interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without
causing a double booking. Otherwise, return false and do not add the event to the calendar.


Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.


Constraints:

0 <= start < end <= 10^9
At most 1000 calls will be made to book.


'''

class MyCalendar(object):

    def __init__(self):
        self.cal = []


    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """

        if self.cal:
            i = 0
            while i < len(self.cal):
                if self.cal[i][1] <= start and i+1 >= len(self.cal):
                    self.cal.append((start, end))
                    self.cal.sort()
                    return True
                i += 1

            j = len(self.cal)-1
            while j >= 0:
                if self.cal[j][0] >= end and j-1 < 0:
                    self.cal.append((start, end))
                    self.cal.sort()
                    return True
                j -= 1
            return False
        else:
            self.cal.append((start, end))

        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

obj = MyCalendar()
start, end = 10, 20
assert True == obj.book(start,end)
start, end = 15, 25
assert False == obj.book(start,end)
start, end = 20, 30
assert True == obj.book(start,end)


# ["MyCalendar","book","book","book","book","book","book","book","book","book","book"]
# [[],[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
obj2 = MyCalendar()
start, end = 47, 50
assert True == obj2.book(start,end)
start, end = 33, 41
assert True == obj2.book(start,end)
start, end = 39, 45
assert False == obj2.book(start,end)
start, end = 33, 42
assert False == obj2.book(start,end)