'''

Given an Iterator class interface with methods: next() and hasNext(),

design and implement a PeekingIterator that support the peek() operation --

it essentially peek() at the element that will be returned by the next call to next().

Example:

Assume that the iterator is initialized to the beginning of the list: [1,2,3].

Call next() gets you 1, the first element in the list.

Now you call peek() and it returns 2, the next element.
Calling next() after that still return 2.
You call next() the final time and it returns 3, the last element.
Calling hasNext() after that should return false.

Follow up:
How would you extend your design to be generic and work with all types,
not just integer?


'''


# Below is the interface for Iterator, which is already defined for you.
#
class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.numsIter = iter(nums)
        self._hasNext = None
        self._nextVal = None

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        if self._hasNext is None:
            try:
                self._nextVal = next(self.numsIter)
            except StopIteration:
                self._hasNext = False
            else:
                self._hasNext = True

        return self._hasNext

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        if self._hasNext:
            result = self._nextVal
        else:
            result = next(self.numsIter)
        self._hasNext = None
        return result


'''
==================================================
'''



class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.peekFlag = False
        self.nextItem = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peekFlag:
            self.nextItem = self.iter.next()
            self.peekFlag = True

        return self.nextItem

    def next(self):
        """
        :rtype: int
        """
        if not self.peekFlag:
            return self.iter.next()
        nextItem = self.nextItem
        self.peekFlag = False
        self.nextItem = None
        return nextItem

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peekFlag or self.iter.hasNext()


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

nums = [1,2,3]
iter = PeekingIterator(Iterator(nums))
print iter
while iter.hasNext():
    val = iter.peek()   # Get the next element but not advance the iterator.
    print val
    iter.next()         # Should return the same value as [val].