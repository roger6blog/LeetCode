'''
Level: Medium

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function,

nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that

the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).

For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target not in nums:
            return -1

        return nums.index(target)


    def search_binary(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums)-1

        if not nums:
            return -1

        while left+1 < right:
            mid = (left+right) // 2
            if nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right

        return -1








nums = [4,5,6,7,0,1,2]
target = 0
assert 4 == Solution().search(nums, target)

nums = [4,5,6,7,0,1,2]
target = 0
assert 4 == Solution().search_binary(nums, target)

nums = [4,5,6,7,0,1,2]
target = 3
assert -1 == Solution().search_binary(nums, target)

nums = [4,5,6,7,8,1,2,3]
target = 8
assert 4 == Solution().search_binary(nums, target)