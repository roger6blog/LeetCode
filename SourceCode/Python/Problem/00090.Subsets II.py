'''
Level: Medium

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.


Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10


'''

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def rec(res, index, nums, path):
            path.sort()
            if path not in res:
                res.append(path)

            for i in range(index, len(nums)):
                if 1 <= i < len(nums)-1 and nums[i] == nums[i+1]:
                    continue
                rec(res, i+1, nums, path+[nums[i]])

        i_nums = [i for i in range(len(nums))]
        res = []
        rec(res, 0, i_nums, [])
        print(res)
        ans = []
        for r in res:
            a = []
            for i in r:
                a += [nums[i]]
            a.sort()
            if a not in ans:
                ans.append(a)

        print(ans)

        return ans
nums = [1,2,2]
Solution().subsetsWithDup(nums)

nums = [4,4,4,1,4]
Solution().subsetsWithDup(nums)
