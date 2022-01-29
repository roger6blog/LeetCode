'''
Level: Easy   Tag: [Design]

Design and implement a TwoSum class.

It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) // return true
find(7) // return false


'''

from collections import defaultdict
class TwoSum(object):

    def __init__(self):
        # initialize your data structure here
        def zero():
            return 0
        self.count = defaultdict(zero)


    # Add the number to an internal data structure.
    # @param number {int}
    # @return nothing
    def add(self, number):

        self.count[number] += 1

    # Find if there exists any pair of numbers which sum is equal to the value.
    # @param value {int}
    # @return true if can be found or false
    def find(self, value):
        for c in self.count:
            # value - c != c 防止需求數等於某數字x2的情況
            if value-c in self.count and (value - c != c or self.count[c] > 1):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)

twoSum = TwoSum()
twoSum.add(1)
twoSum.add(3)
twoSum.add(5)
twoSum.add(5)

print(twoSum.find(4))
print(twoSum.find(7))
print(twoSum.find(10))