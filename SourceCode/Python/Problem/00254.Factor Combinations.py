'''
Level: Medium

Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

You may assume that n is always positive.
Factors should be greater than 1 and less than n.

Example1

Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
Explanation:
2*6 = 12
2*2*3 = 12
3*4 = 12

Example2

Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
Explanation:
2*16=32
2*2*8=32
2*2*2*4=32
2*2*2*2*2=32
2*4*4=32
4*8=32

'''
class Solution:
    def getFactors(self, n):
        """
        @param n: a integer
        @return: return a 2D array
        """
        def rec(res, nums, curr, target):
            p = 1
            for c in curr:
                p *= c
            if p == target:
                curr.sort()
                if curr not in res:
                    res.append(curr)
                    return

            elif p > target:
                return

            for i in range(len(nums)):
                rec(res, nums, curr+[nums[i]], target)


        nums = [i+1 for i in range(1, n//2)]
        ans = []
        rec(ans, nums, [], n)

        print(ans)
        return ans



n = 12
Solution().getFactors(n)
n = 32
Solution().getFactors(n)