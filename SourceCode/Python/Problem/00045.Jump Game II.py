'''
Level: Medium
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


Constraints:

1 <= nums.length <= 10^4
0 <= nums[i] <= 1000

'''

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        reached = 0
        goal = 0
        steps = 0
        for i in range(len(nums)-1):
            if i <= reached:
                reached = max(reached, i + nums[i])
            if i == goal:
                steps += 1
                goal = reached

        return steps




nums = [2,3,1,1,4]
assert 2 == Solution().jump(nums)
nums = [2,3,0,1,4]
assert 2 == Solution().jump(nums)