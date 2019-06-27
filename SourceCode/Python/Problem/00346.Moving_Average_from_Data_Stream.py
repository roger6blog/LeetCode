'''

Given a stream of integers and a window size,

calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3


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


size = 3
obj = MovingAverage(size)
print obj.next(1)
print obj.next(10)
print obj.next(3)
print obj.next(5)


