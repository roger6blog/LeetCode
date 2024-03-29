'''
Level: Medium   Tag: [Design]

Implement an iterator to flatten a 2d vector.

For example, Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,2,3,4,5,6].

Example 2:

Input:[[7,9],[5]]
Output:[7,9,5]

Hint:

1. How many variables do you need to keep track?
2. Two variables is all you need. Try with x and y.
3. Beware of empty rows. It could be the first few rows.
4. To write correct code, think about the invariant to maintain. What is it?
5. The invariant is x and y must always point to a valid point in the 2d vector.
   Should you maintain your invariant ahead of time or right when you need it?
6. Not sure? Think about how you would implement hasNext(). Which is more complex?
7. Common logic in two different places should be refactored into a common method.

Follow up:
As an added challenge, try to code it using only iterators in C++ or iterators in Java.
'''

class Vector2D:
    vec = None

    # Initialize your data structure here.
    # @param {integer[][]} vec2d
    def __init__(self, vec2d):
        self.x = iter(vec2d)

    def next(self):
        return self.val

    def hasNext(self):
        if not hasattr(self, 'y'):
            try:
                self.y = iter(self.x.next())
            except StopIteration:
                return False


        try:
            self.val = self.y.next()
        except StopIteration:
            del self.y
            return self.hasNext()

        return True


i = Vector2D([
  [1,2],
  [3],
  [],
  [4,5,6],
  []
])


while i.hasNext():
    print(i.next())


class Vector2D2(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        self.vec2d = vec2d


    # @return {int} a next element
    def next(self):
        ret = None
        for n in self.vec2d:
            ret = n.pop(0)
            if n == []:
                self.vec2d.pop(0)
            break

        return ret



    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        if self.vec2d:
            return True
        return False


# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
vec2d = [
  [1,2],
  [3],
  [4,5,6]
]
i, v = Vector2D2(vec2d), []
while i.hasNext():
    v.append(i.next())
print(v)