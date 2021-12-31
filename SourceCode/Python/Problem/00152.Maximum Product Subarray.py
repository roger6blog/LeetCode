'''
Level: Medium
Given an integer array nums,
find a contiguous non-empty subarray within the array that has the largest product,
and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


'''


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        ans = float('-inf')

        curr_max = nums[0]
        curr_min = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            curr_prod = curr_max
            curr_max = max(curr_max*nums[i], curr_min*nums[i], nums[i])
            curr_min = min(curr_prod*nums[i], curr_min*nums[i], nums[i])

            ans = max(curr_max, ans)

        print(ans)
        return ans

nums = [2,3,-2,4]
assert 6 == Solution().maxProduct(nums)

nums = [-2,0,-1]
assert 0 == Solution().maxProduct(nums)

nums = [-3,-1,-1]
assert 3 == Solution().maxProduct(nums)

nums = [0,2]
assert 2 == Solution().maxProduct(nums)

nums = [3,-1,4]
assert 4 == Solution().maxProduct(nums)

nums = [2,-5,-2,-4,3]
assert 24 == Solution().maxProduct(nums)

nums = [2,-1,1,1]
assert 2 == Solution().maxProduct(nums)