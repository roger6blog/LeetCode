'''
Level: Medium  Tag: [Binary Search]

Given an array of integers nums sorted in non-decreasing order,

find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9

'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(nums) == 1:
            if target == nums[0]:
                return [0, 0]
        left = 0
        right = len(nums)-1
        found = -1
        while left <= right:
            mid = left + (right-left)//2

            if nums[mid] == target:
                found = mid
                break

            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1

        if found == -1:
            return [-1, -1]

        lower = found
        upper = found
        while lower-1 >= 0:
            if nums[lower-1] != nums[found]:
                break
            lower -= 1

        while upper+1 < len(nums):
            if nums[upper+1] != nums[found]:
                break
            upper += 1

        print([lower, upper])
        return([lower, upper])


    def searchRange_bisect(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        import bisect
        start = bisect.bisect_left(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = bisect.bisect_right(nums, target)
        return [start, end-1]


nums = [5,7,7,8,8,10]
target = 8
assert [3,4] == Solution().searchRange(nums, target)
Solution().searchRange_bisect(nums, target)

nums = [1]
target = 1
Solution().searchRange_bisect(nums, target)
nums = [5,7,7,8,8,10]
target = 6
assert [-1,-1] == Solution().searchRange(nums, target)

nums = [1]
target = 1
assert [0,0] == Solution().searchRange(nums, target)

nums = [2,2]
target = 2
assert [0,1] == Solution().searchRange(nums, target)

nums = [1,4]
target = 4
assert [1,1] == Solution().searchRange(nums, target)