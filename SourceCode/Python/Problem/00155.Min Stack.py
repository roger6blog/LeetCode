'''
Level: Easy   Tag: [Stack]

Design a stack that supports push, pop, top,
and retrieving the minimum element in constant time.

MinStack() initializes the stack object.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[     [],     [-2],  [0],   [-3],   [],     [],   [],    []]

Output
[null,null,null,null,-3,null,0,-2]

Explaination
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

Constraints:

-2^31 <= val <= 2^31 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 10^4 calls will be made to push, pop, top, and getMin.

'''

import heapq
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minList = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        self.minList.append(x)
        self.minList.sort()


    def pop(self):
        """
        :rtype: void
        """
        x = self.stack[-1]
        self.stack.pop()
        self.minList.remove(x)
        self.minList.sort()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minList[0]





# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())