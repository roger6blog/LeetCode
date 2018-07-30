'''

Given an array of integers and an integer k,

you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

'''

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # prefixSum[i] = prefixSum[i-1] + num[x]
        # ==> k = prefixSum[i] - prefixSum[i-1]

        length = len(nums)
        prefixSum = {}
        prefixSum[0] = 1
        sum = 0
        count = 0

        for num in nums:
            sum += num
            if sum - k in prefixSum: # It means new sum - old sum == k
                count += prefixSum[sum - k]
            if sum not in prefixSum:
                prefixSum[sum] = 1
            else:
                prefixSum[sum] += 1

        return count





nums = [1,1,1]
k = 2

print Solution().subarraySum(nums, k)