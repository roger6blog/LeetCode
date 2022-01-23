'''
2021後被Locked
Level:Easy   Tag: [Design]

Given a stream of integers and a window size,

calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1 // return 1.00000
m.next(10) = (1 + 10) / 2 // return 5.50000
m.next(3) = (1 + 10 + 3) / 3 // return 4.66667
m.next(5) = (10 + 3 + 5) / 3 // return 6.00000


'''

class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = []
        self.maxsize = size
    def next(self, num):
        if len(self.queue) == self.maxsize:
            self.queue = self.queue[1:]
        self.queue.append(num)
        return sum(self.queue) / len(self.queue)

from collections import deque
class MovingAverage2(object):
    def __init__(self, size):
        self.queue = deque()
        self.size = size

    def next(self, num):
        if len(self.queue) > self.size:
            self.queue.popleft()

        self.queue.append(num)
        ans = sum(self.queue) // len(self.queue)
        # print(ans)

        return ans
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)


size = 3
obj = MovingAverage(size)
print(obj.next(1))
print(obj.next(10))
print(obj.next(3))
print(obj.next(5))
obj2 = MovingAverage(size)
print(obj2.next(1))
print(obj2.next(10))
print(obj2.next(3))
print(obj2.next(5))


