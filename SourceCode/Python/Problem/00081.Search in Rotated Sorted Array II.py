'''
Level: Medium

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function,

nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that

the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).

For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.



Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104


Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?


'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        if target in nums:
            return True

        return False

    def search_binary(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        left = 0
        right = len(nums)-1

        while left+1 < right:
            mid = left + (right-left) // 2

            if nums[mid] > nums[right]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid+1
            elif nums[right] > nums[mid]:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid-1
            else:
                right -= 1

        if nums[left] == target:
            return True

        if nums[right] == target:
            return True

        return False

nums = [2,5,6,0,0,1,2]
target = 0
assert True == Solution().search(nums, target)
nums = [2,5,6,0,0,1,2]
target = 0
assert True == Solution().search_binary(nums, target)

nums = [1,0,1,1,1]
target = 0
assert True == Solution().search_binary(nums, target)

nums = [2,2,2,3,2,2,2]
target = 3
assert True == Solution().search_binary(nums, target)

nums = [2,2,2,0,2,2]
target = 0
assert True == Solution().search_binary(nums, target)