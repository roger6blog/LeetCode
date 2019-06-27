'''

Median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) -
Add a integer number from the data stream to the data structure.

double findMedian() -
Return the median of all elements so far.

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2


'''

# This algorithm will cause TLE (Time Limit Exceed)
class MedianFinder_TLE(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if num == None:
            return

        self.nums.append(num)
        self.nums.sort()

    def findMedian(self):
        """
        :rtype: float
        """

        length = len(self.nums)
        if length == 1:
            return self.nums[0]

        if length % 2 == 0:
            mid = length / 2
            return (self.nums[mid] + self.nums[mid - 1]) / 2.0
        else:
            mid = (length) / 2
            return float(self.nums[mid])


import heapq
class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = [float('inf')]
        self.maxHeap = []
        self.a = self.minHeap[0]
        print self.a

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.maxHeap, -num)
        if len(self.minHeap):
            minTop = self.minHeap[0]
        else:
            minTop = None

        if len(self.maxHeap):
            maxTop = self.maxHeap[0]
        else:
            maxTop = None

        if minTop < -maxTop or len(self.minHeap) + 1 < len(self.maxHeap):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        if len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))


    def findMedian(self):
        """
        :rtype: float
        """

        if len(self.minHeap) < len(self.maxHeap):
            return -1.0 * self.maxHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
'''
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
'''

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print obj.findMedian()
obj.addNum(3)
print obj.findMedian()