'''
Level: Medium

Find all possible combinations of k numbers that add up to a number n,

given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]


Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.


Constraints:

2 <= k <= 9
1 <= n <= 60
'''


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        ans = []
        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.combination(k, n, digits, [], ans)
        return ans


    def combination(self, k, n, digits, current, ans):
        if len(current) > k:
            return

        if current:
            s = sum(current)
        else:
            s = 0

        if s > n:
            return
        elif s == n:
            if len(current) != k:
                return

            current.sort()
            ans.append(current)
        else:
            for c, i in enumerate(digits):
                self.combination(k, n, digits[c+1:], current + [i], ans)





    def combinationSum33(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def rec(res, index, nums, curr, target, k):
            if len(curr) > k:
                return
            s = sum(curr)
            if s == target and len(curr) == k:
                curr.sort()
                if curr not in res:
                    res.append(curr)
                    return

            elif s > target:
                return

            for i in range(index, len(nums)):
                rec(res, i+1, nums, curr+[nums[i]], target, k)


        nums = [i+1 for i in range(9)]

        ans = []
        rec(ans, 0, nums, [], n, k)
        print(ans)

        return ans



k = 3
n = 7
print(Solution().combinationSum3(k, n))




k = 3
n = 7
assert [[1, 2, 4]] == Solution().combinationSum33(k, n)


k = 2
n = 18
Solution().combinationSum33(k, n)