'''
Level: Medium  Tags: [Sliding window]
Given an array of positive integers nums and a positive integer target,
return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1,
numsr] of which the sum is greater than or equal to target.
If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.


Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105


Follow up:
If you have figured out the O(n) solution,
try coding another solution of which the time complexity is O(n log(n)).

'''

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        min_len = float('inf')
        left = 0
        right = len(nums)
        curr_sum = 0

        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_len = min(min_len, right-left+1)
                curr_sum -= nums[left]
                left += 1

        if min_len == float('inf'):
            min_len = 0

        print(min_len)
        return min_len


nums = [2,3,1,2,4,3]
target = 7


assert 2 == Solution().minSubArrayLen(target, nums)

target = 4
nums = [1,4,4]
assert 1 == Solution().minSubArrayLen(target, nums)

target = 11
nums = [1,1,1,1,1,1,1,1]
assert 0 == Solution().minSubArrayLen(target, nums)

target = 11
nums = [1,2,3,4,5]
assert 3 == Solution().minSubArrayLen(target, nums)