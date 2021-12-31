'''
Level: Medium

Given an array nums and a target value k,

find the maximum length of a subarray that sums to k.

If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?


'''

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        prefix_sum = {}  # prefix mapping max_len
        curr_sum = 0
        max_len = 0
        for x in range(len(nums)):
            curr_sum += nums[x]
            if curr_sum - k in prefix_sum:
                max_len = max(max_len, x-prefix_sum[curr_sum-k])

            if curr_sum == k:
                max_len = x + 1

            if curr_sum not in prefix_sum:
                prefix_sum[curr_sum] = x

        print(max_len)
        return max_len



nums = [1, -1, 5, -2, 3]
k = 3
assert 4 == Solution().maxSubArrayLen(nums, k)
nums = [-2, -1, 2, 1]
k = 1
print(Solution().maxSubArrayLen(nums, k))