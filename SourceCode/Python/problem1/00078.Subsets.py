'''

Given a set of distinct integers, nums,

return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]


'''


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.subsetRec(nums, 0, ans, [])
        return ans

    def subsetRec(self, nums, index, ans, path):
        ans.append(path)
        for i in xrange(index, len(nums)):
            self.subsetRec(nums, i+1, ans, path + [nums[i]])

nums = [1,2,3]
print Solution().subsets(nums)