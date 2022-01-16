'''
Level: Easy

Given a sorted array of distinct integers and a target value, return the index if the target is found.

If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4

'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[0] > target:
            return 0

        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) / 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else: # Equal condition
                return mid

        return left


nums = [1,3,5,6]
target = 5
assert 2 == Solution().searchInsert(nums, target)
nums = [1,3,5,6]
target = 2
assert 1 == Solution().searchInsert(nums, target)
nums = [1,3,5,6]
target = 7
assert 4 == Solution().searchInsert(nums, target)
nums = [1,3]
target = 2
assert 1 == Solution().searchInsert(nums, target)
nums = [1,3,5,6]
target = 0
assert 0 == Solution().searchInsert(nums, target)