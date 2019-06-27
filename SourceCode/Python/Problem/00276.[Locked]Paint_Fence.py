'''

There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.


'''

class Solution(object):
    def numWays2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0: return 0
        if n == 1: return k

        # for the first 2 posts
        sameColor = k
        diffColor = k * (k - 1)

        for i in range(2, n):
            temp = diffColor
            diffColor = (sameColor + diffColor) * (k - 1)
            sameColor = temp

        return sameColor + diffColor

    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        diff = [0]*(n+1)
        diff[1] = k
        diff[2] = k*(k-1)

        for i in xrange(3, n+1):
            diff[i] = (diff[i-1] + diff[i-2]) * (k-1)
        same = diff[n - 1]
        return diff[n] + same

n=7
k=3
print Solution().numWays(n, k)
print Solution().numWays2(n, k)