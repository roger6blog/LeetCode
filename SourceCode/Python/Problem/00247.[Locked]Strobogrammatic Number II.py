'''
Level: Medium

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"].

Example 2:

Input: n = 1,
Output: ["0","1","8"]

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

        # @param {integer} n
        # @return {string[]}
    def findStrobogrammatic2(self, n):
        """
        受瓶子倒水那道题的启发 直接BFS即可 而且这道题用BFS没什么缺点
        memory上由于答案本来就要求所有解 所以无论如何都是O(答案个数)
        优点的话 免去递归 并且比较好理解 唯一一个corner case注意一下
        数首不可以是0除非n是1
        """
        from collections import deque
        lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}

        queue = deque()
        if n % 2 == 0:
            queue.append("")
        else:
            queue.append("0")
            queue.append("1")
            queue.append("8")


        ans = []
        while queue:
            num = queue.popleft()
            if len(num) == n:
                if num[0] != 0 or n == 1:
                    ans += [num]

            else:
                for k, v in lookup.items():
                    queue.append(k + num + v)

        print(ans)
        return ans









print Solution().findStrobogrammatic2(6)