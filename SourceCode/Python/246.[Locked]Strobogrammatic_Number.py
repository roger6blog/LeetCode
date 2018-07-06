'''

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.

'''

class Solution:
    def __init__(self):
        self.lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}

    # @param {string} num
    # @return {boolean}
    def isStrobogrammatic(self, num):
        mid = len(num) / 2
        for x in xrange(mid, -1, -1):
            if num[x] not in self.lookup or num[mid+mid-x] not in self.lookup:
                return False
            if self.lookup[num[x]] != num[mid+mid-x]:
                print("Fail: {} vs {}".format(self.lookup[num[x]], self.lookup[num[mid+mid-x]]))
                return False

        return True



a = '18181'
print Solution().isStrobogrammatic(a)