'''
Level: Medium   Tag: [Math]

Given an array of n integers nums and a target,

find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition
nums[i] + nums[j] + nums[k] < target.


Example1

Input:  nums = [-2,0,1,3], target = 2
Output: 2
Explanation:
Because there are two triplets which sums are less than 2:
[-2, 0, 1]
[-2, 0, 3]

Example2

Input: nums = [-2,0,-1,3], target = 2
Output: 3
Explanation:
Because there are three triplets which sums are less than 2:
[-2, 0, -1]
[-2, 0, 3]
[-2, -1, 3]

Follow up:
Could you solve it in O(n^2) runtime?


'''


class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """
    def threeSumSmaller(self, nums, target):
        # Write your code here
        ans = 0
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                if sums < target:
                    ans += right - left # 在left和right區間的數字和也必定小於target
                    left += 1
                else:
                    right -= 1

        print(ans)

        return ans


nums = [-2,0,1,3]
target = 2
assert 2 == Solution().threeSumSmaller(nums, target)

nums = [-2,0,-1,3]
target = 2
Solution().threeSumSmaller(nums, target)