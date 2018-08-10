'''

Given a set of distinct positive integers,

find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]
Result: [1,2] (of course, [1,3] will also be ok)

Example 2:

nums: [1,2,4,8]
Result: [1,2,4,8]


Credits:
Special thanks to @Stomach_ache for adding this problem and creating all test cases.


'''


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums.sort()
        length = len(nums)
        dp = [0] * length
        max = 0
        max_index = 0
        child = [0] * length
        ans = []

        for i in xrange(length-1, -1, -1):
            for j in xrange(i, length):
                if nums[j] % nums[i] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    child[i] = j

                    # To store max subset length and relative start point index
                    if max < dp[i]:
                        max = dp[i]
                        max_index = i

        # Construct output subset
        for k in xrange(max):
            ans.append(nums[max_index])
            max_index = child[max_index]

        return ans


nums = [1,2,3,4]
print Solution().largestDivisibleSubset(nums)
