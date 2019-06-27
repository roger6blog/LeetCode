'''

Given an array of integers,
return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

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

nums = [11 , 2, 15, 7  ]
target = 9
print Solution().twoSum(nums, target)