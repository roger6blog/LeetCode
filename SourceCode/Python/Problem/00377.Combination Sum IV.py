'''
Level: Medium

Given an distinct integer array with all positive numbers and no duplicates,

find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.

Example 2:

Input: nums = [9], target = 3
Output: 0


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.


'''


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [1] + [0] * target
        for i in xrange(target + 1):
            for x in nums:
                if i + x <= target:
                    # dp[i+x] = sum(dp[i+x - x])
                    dp[i+x] += dp[i]

        return dp[target]






    def combinationSum44(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


        def rec(res, index, nums, curr, target):
            s = sum(curr)
            if s == target:
                if curr not in res:
                    res.append(curr)
            elif s > target:
                return

            for i in range(len(nums)):
                rec(res, i+1, nums, curr+[nums[i]], target)

        ans = []
        rec(ans, 0, nums, [], target)
        print(ans)
        return ans

nums = [1, 2, 3]
target = 4

# nums = [4,2,1]
# target = 32

# print(Solution().combinationSum4(nums, target))
print(Solution().combinationSum44(nums, target))


