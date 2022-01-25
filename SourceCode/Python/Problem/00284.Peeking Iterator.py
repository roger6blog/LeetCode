'''
Level: Medium     Tag: [Design]

Design an iterator that supports the peek operation on an existing iterator in addition to the hasNext and the next operations.

Implement the PeekingIterator class:

PeekingIterator(Iterator<int> nums) Initializes the object with the given integer iterator iterator.
int next() Returns the next element in the array and moves the pointer to the next element.
boolean hasNext() Returns true if there are still elements in the array.
int peek() Returns the next element in the array without moving the pointer.
Note: Each language may have a different implementation of the constructor and Iterator, but they all support the int next() and boolean hasNext() functions.

Example 1:

Input
["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 2, 2, 3, false]

Explanation
PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [1,2,3]
peekingIterator.next();    // return 1, the pointer moves to the next element [1,2,3].
peekingIterator.peek();    // return 2, the pointer does not move [1,2,3].
peekingIterator.next();    // return 2, the pointer moves to the next element [1,2,3]
peekingIterator.next();    // return 3, the pointer moves to the next element [1,2,3]
peekingIterator.hasNext(); // return False


Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 1000
All the calls to next and peek are valid.
At most 1000 calls will be made to next, hasNext, and peek.


Follow up: How would you extend your design to be generic and work with all types, not just integer?




====================  Old Description  ==========================



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








class PeekingIterator2(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.peek = None


    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peek:
            return self.peek
        if self.iter.hasNext():
            self.peek = self.iter.next()
        return self.peek


    def next(self):
        """
        :rtype: int
        """
        ret = self.peek
        if self.peek:
            self.peek = None
            return ret
        return self.iter.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return (self.peek is not None) or self.iter.hasNext()




# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].


iter = PeekingIterator2(Iterator(nums))
while iter.hasNext():
    val = iter.peek()   # Get the next element but not advance the iterator.
    iter.next()         # Should return the same value as [val].
