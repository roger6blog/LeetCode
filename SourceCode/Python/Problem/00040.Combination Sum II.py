'''
Level: Medium

Given a collection of candidate numbers (candidates) and a target number (target),

find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]


'''


class Solution(object):
    def combinationSum2_TLE(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if candidates == []:
            return []
        ans = []
        self.combination(candidates, target, [], ans)
        bSet = set(map(tuple, ans))
        return map(list, bSet)

    def combination(self, candidates, target, current, ans):
        if current:
            s = sum(current)
        else:
            s = 0

        if s > target:
            return
        elif s == target:
            current.sort()
            ans.append(current)
            return
        else:
            for c, i in enumerate(candidates):
                self.combination(candidates[c+1:], target, current + [i], ans)







    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """


        def rec(res, index, nums, curr, target, used):
            if curr:
                s = sum(curr)
            else:
                s = 0

            if s == target:
                curr.sort()
                if curr not in ans:
                    res.append(curr[:])
            elif s > target:
                return

            for i in xrange(index, len(nums)):
                if i != index and nums[i-1] == nums[i] and not used[i]:
                    continue

                used[i] = True
                curr.append(nums[i])
                rec(res, i+1, nums, curr, target, used)
                used[i] = False
                curr.pop()

        used = [False] * len(candidates)
        candidates.sort()
        ans = []
        rec(ans, 0, candidates, [], target, used)

        print(ans)
        return ans


candidates = [10,1,2,7,6,1,5]
target = 8
# print(Solution().combinationSum2(candidates, target))
assert [[1,1,6],[1,2,5],[1,7],[2,6]] == Solution().combinationSum2(candidates, target)

candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target = 27
assert [] == Solution().combinationSum2(candidates, target)
