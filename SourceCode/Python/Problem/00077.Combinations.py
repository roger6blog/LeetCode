'''
Level: Medium

Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:

Input: n = 1, k = 1
Output: [[1]]


Constraints:

1 <= n <= 20
1 <= k <= n


'''

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def rec(res, index, nums, path, k):
            if len(path) == k:
                path.sort()
                res.append(path)

            for i in range(index, len(nums)):
                if len(path+[nums[i]]) > k:
                    continue
                rec(res, i+1, nums, path+[nums[i]], k)

        nums = [i+1 for i in range(n)]
        ans = []
        rec(ans, 0, nums, [], k)
        print(ans)
        return ans

    def combine2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        from itertools import combinations

        nums = [i+1 for i in range(n)]
        ans = list(combinations(nums, k))
        print(ans)
        return ans

n = 4
k = 2
Solution().combine(n, k)
Solution().combine2(n, k)