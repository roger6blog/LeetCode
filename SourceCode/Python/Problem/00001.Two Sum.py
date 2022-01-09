'''
Level: Easy

Given an array of integers,
return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dicBuff = {}
        for i in xrange(len(nums)):
            if target - nums[i] in dicBuff:
                # print("nums[{}] == {}".format(i, nums[i]))
                return [i, dicBuff[target - nums[i]]]
            else:
                dicBuff[nums[i]] = i
                # print("dicBuff[{}] == {}".format(nums[i], i))

    def twoSum2(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            else:
                dic[target - num] = i



    def twoSum3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        another_num_map = {}
        for i in range(len(nums)):
            if nums[i] not in another_num_map:
                another_num_map[target - nums[i]] = i
            else:
                ans = [another_num_map[nums[i]], i]



        return ans






nums = [11, 2, 15, 7]
target = 9
print(Solution().twoSum(nums, target))
nums = [11, 2, 15, 7]
target = 9
print(Solution().twoSum2(nums, target))

nums = [3,2,4]
target = 6
print(Solution().twoSum2(nums, target))