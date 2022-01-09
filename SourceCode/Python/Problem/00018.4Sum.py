'''
Level: Medium

Given an array nums of n integers, r

eturn an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


Constraints:

1 <= nums.length <= 200
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9

'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        target_map = []
        for i in range(len(nums)-1):
            target_map.append(target - (nums[i] + nums[i+1]))

aa
        candidate = []
        for t in range(len(target_map)):
            another_num_map = {}
            for i in range(t+1, len(nums)):
                if nums[i] not in another_num_map:
                    another_num_map[target_map[t] - nums[i]] = i
                else:
                    x = t // 2
                    y = t // 2 + 1
                    candidate.append([nums[x], nums[y], nums[i], nums[another_num_map[nums[i]]]])

        ans = []

nums = [1,0,-1,0,-2,2]
target = 0
Solution().fourSum(nums, target)