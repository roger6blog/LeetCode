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


        def rec(count, cache, nums, curr, target):
            if curr in cache:
                return cache[curr]
            if curr == target:
                return 1
            elif curr > target:
                return 0
            count = 0
            for i in range(len(nums)):
                count += rec(count, cache, nums, curr+nums[i], target)
            cache[curr] = count

            return count

        ans = rec(0, {}, nums, 0, target)
        print(ans)
        return ans

nums = [1, 2, 3]
target = 4

# nums = [4,2,1]
# target = 32

# print(Solution().combinationSum4(nums, target))
assert 7 == Solution().combinationSum44(nums, target)


nums = [1,50]
target = 200
assert 28730 == Solution().combinationSum44(nums, target)

[4,2,1]
32
print(Solution().combinationSum44(nums, target))