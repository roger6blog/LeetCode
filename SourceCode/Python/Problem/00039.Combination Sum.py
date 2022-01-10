'''
Level: Medium

Given an array of distinct integers candidates and a target integer target,

return a list of all unique combinations of candidates where the chosen numbers sum to target.

You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.

Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []


Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500


'''

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        ans = []

        self.combination(candidates, target, [], ans)
        return  ans

    def combination(self, candidates, target, current, ans):
        if current:
            s = sum(current)
        else:
            s = 0


        if s > target:
            # End of recursive
            return
        elif s == target:
            ans.append(current)
            return
        else:
            for c, i in enumerate(candidates):
                self.combination(candidates[c:], target, current + [i], ans)



    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def rec(res, nums, curr, target):
            s = sum(curr)
            if s == target:
                curr.sort()
                if curr not in res:
                    res.append(curr)
                return
            elif s > target:
                return

            for i in range(len(nums)):
                rec(res, nums, curr+[nums[i]], target)

        candidates.sort()
        ans = []
        rec(ans, candidates, [], target)

        print(ans)
        return ans

candidates = [2,3,6,7]
target = 7


# candidates = [2,3,5]
# target = 8
print Solution().combinationSum(candidates, target)

candidates = [2,3,6,7]
target = 7
Solution().combinationSum2(candidates, target)