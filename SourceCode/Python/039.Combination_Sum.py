'''

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),

find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]


Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]


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


candidates = [2,3,6,7]
target = 7


# candidates = [2,3,5]
# target = 8
print Solution().combinationSum(candidates, target)