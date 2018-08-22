'''

Given an array consisting of n integers,

find the contiguous subarray of given length k that has the maximum average value.

And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].


'''

import sys
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sums = 0
        ans = -sys.maxint - 1
        for i in xrange(len(nums)):
            sums += nums[i]
            if i+1 > k:
                sums -= nums[i-k]
            if i+1 >= k:
                ans = max(ans, sums)

        return float(ans) / k



    def findMaxAverageTLE(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        ans = -sys.maxint - 1
        for i in xrange(len(nums)):
            if len(nums[i:i+k]) < k:
                break
            ans = max(ans, sum(nums[i:i+k]))
        return float(ans)/k

nums = [1,12,-5,-6,50,3]
k = 4
x = [5]
print Solution().findMaxAverage(x, 1)