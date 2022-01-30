'''
Level: Medium   Tag: [Math]

Given an integer array nums of length n and an integer target,

find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:

Input: nums = [0,0,0], target = 1
Output: 0


Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-10^4 <= target <= 10^4


'''


'''
先排序好
依序取一點
接著取這一點之外的兩個端點來逼近最接近target的三個數字之和
'''

from collections import defaultdict

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        ans = None
        nearest = float('inf')
        for i in range(n):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                if abs(target-sums) < nearest:
                    nearest = abs(target-sums)
                    ans = sums
                if sums > target:
                    right -= 1
                else:
                    left += 1

        print(ans)

        return ans

nums = [-1,2,1,-4]
target = 1
Solution().threeSumClosest(nums, target)