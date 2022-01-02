'''
Level: Easy

Given an array nums,

write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]


Example 2:

Input: nums = [0]
Output: [0]

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.


'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left = 0
        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1



# nums = [0,1,0,3,12]
nums = [0, 1, 0 , 3]
Solution().moveZeroes(nums)
print(nums)