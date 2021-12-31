'''

Given an integer array nums,
return an array answer such that
answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)

'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        total_prod = 1
        zero_count = 0
        for i in nums:
            if i == 0:
                zero_count += 1
                continue
            total_prod *= i

        for i in range(len(nums)):
            if nums[i] == 0:
                if zero_count > 1:
                    nums[i] = 0
                else:
                    nums[i] = total_prod
            else:
                if zero_count:
                    nums[i] = 0
                else:
                    nums[i] = total_prod / nums[i]

        print(nums)
        return nums




nums = [1,2,3,4]
assert [24,12,8,6] == Solution().productExceptSelf(nums)

nums = [-1,1,0,-3,3]
assert [0,0,9,0,0] == Solution().productExceptSelf(nums)