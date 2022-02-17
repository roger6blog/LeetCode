'''
Level: Easy Tags: [Greedy]
Given an integer array nums,
find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23


Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4


Follow up: If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach,
which is more subtle.

'''

class Solution(object):
    def maxSubArray_TLE(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        ans = float('-inf')

        for i in range(len(nums)):
            for j in range(len(nums)+1):
                if i >= j:
                    continue
                ans = max(ans, sum(nums[i:j]))

        print(ans)
        return ans


    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        Greedy method
        1. Add element to sums
        2. Compare maximun of ans and sums
        3. If sums < 0, it means sums of this slice will make total sum more less,
           so we give up this slice sums and keep iteration by counting a new sums.
        '''
        if len(nums) == 1:
            return nums[0]
        ans = float('-inf')

        sums = 0
        for n in nums:
            sums += n
            ans = max(ans, sums)
            sums = max(sums, 0)

        return ans

nums = [-2,1,-3,4,-1,2,1,-5,4]
assert 6 == Solution().maxSubArray(nums)
nums = [5,4,-1,7,8]
assert 23 == Solution().maxSubArray(nums)
nums = [-2,-1]
assert -1 == Solution().maxSubArray(nums)