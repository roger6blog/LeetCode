'''

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"].

Hint:

Try to use recursion and notice that it should recurse with n - 2 instead of n - 1.

'''

class Solution:
    lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}

    # @param {integer} n
    # @return {string[]}
    def findStrobogrammatic(self, n):
        return self.findStrobogrammaticRecu(n, n)

    def findStrobogrammaticRecu(self, n, k):
        if k == 0:
            return ['']
        if k == 1:
            return ['0', '1', '8']
        ans = []
        for num in self.findStrobogrammaticRecu(n, k-2):
            for key, value in self.lookup.iteritems():
                #if n != k or key != '0': # I'm not sure why need n != k
                if key != '0':
                    ans.append(key+num+value)
        return ans

print Solution().findStrobogrammatic(1)