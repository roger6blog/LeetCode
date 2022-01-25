'''
Level: Medium   Tag: [Design]

Given two 1d vectors, implement an iterator to return their elements alternately.

For example, given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

Follow up: What if you are given k 1d vectors?
How well can your code be extended to such cases?

Clarification for the follow up question - Update (2015-09-18):
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases.
If "Zigzag" does not look right to you,
replace "Zigzag" with "Cyclic".
For example, given the following input:

[1,2,3]
[4,5,6,7]
[8,9]
It should return [1,4,8,2,5,9,3,6,7].


'''


class ZigzagIterator(object):
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        ans = []
        v1Iter = iter(v1)
        v2Iter = iter(v2)
        keepV1 = True
        keepV2 = True
        while (keepV1 or keepV2):
            try:
                ans.append(v1Iter.next())
            except StopIteration:
                keepV1 = False
            try:
                ans.append(v2Iter.next())
            except StopIteration:
                keepV2 = False

        print(ans)


v1 = [1, 2]
v2 = [3, 4, 5, 6]
ZigzagIterator(v1, v2)



from collections import deque
class ZigzagIterator2:

    # @param {int[]} v1 v2 two 1d vectors
    def __init__(self, v1, v2):
        # initialize your data structure here
        self.z1 = deque(v1)
        self.z2 = deque(v2)
        self.last_v = 0



    def next(self):
        # Write your code here
        self.last_v += 1
        if self.last_v % 2 == 1:
            if self.z1:
                return self.z1.popleft()
            else:
                return self.z2.popleft()
        else:
            if self.z2:
                return self.z2.popleft()
            else:
                return self.z1.popleft()




    def hasNext(self):
        # Write your code here
        return self.z1 or self.z2

# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result

solution, result = ZigzagIterator2(v1, v2), []
while solution.hasNext():
    result.append(solution.next())
print(result)
