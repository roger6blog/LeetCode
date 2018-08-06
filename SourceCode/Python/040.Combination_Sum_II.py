'''

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
    def combinationSum2(self, candidates, target):
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







candidates = [10,1,2,7,6,1,5]
target = 8
print Solution().combinationSum2(candidates, target)