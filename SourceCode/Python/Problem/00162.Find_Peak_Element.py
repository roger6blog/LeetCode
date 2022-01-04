'''
Level: Medium

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.

Note:

Your solution should be in logarithmic complexity.

'''

# Use binary search to handle four Conditions:
#     1. array length is 1  -> return the only index
#     2. array length is 2  -> return the bigger number's index
#     3. array length is bigger than 2 ->
#           (1) find mid, compare it with its left and right neighbors
#           (2) return mid if nums[mid] greater than both neighbors
#           (3) take the right half array if nums[mid] smaller than right neighbor
#           (4) otherwise, take the left half

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1

        # handle condition 3
        while left < right - 1:
            mid = (left + right) / 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        # handle condition 1 and 2
        return left if nums[left] >= nums[right] else right



    def findPeakElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return 0

        if len(nums) == 2:
            return nums.index(max(nums))

        left = 0
        right = len(nums)-1

        while left < right:
            mid = left + (right-left)//2

            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid

            if nums[mid+1] > nums[mid]:
                left = mid+1

            else:
                right = mid-1

        return left if nums[left] >= nums[right] else right



a = [1,2,3,1]
sol = Solution()
assert 2 == sol.findPeakElement2(a)


nums = [1,2,1,3,5,6,4]
assert 5 == Solution().findPeakElement2(nums)

nums = [1,2]
assert 1 == Solution().findPeakElement2(nums)

nums = [6,5,4,3,2,3,2]
assert 0 == Solution().findPeakElement2(nums)

nums = [1,2,3]
assert 2 == Solution().findPeakElement2(nums)


nums = [5,4,3,4,5]
assert 4 == Solution().findPeakElement2(nums)