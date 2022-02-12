'''
Level: Medium

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

 For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].



Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:

1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4


Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?



'''

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        max_sub = [nums[0]]

        for n in nums[1:]:
            if n > max_sub[-1]:
                max_sub.append(n)
            elif n < max_sub[-1]:
                i = bisect.bisect_left(max_sub, n)
                max_sub[i] = n

        print(len(max_sub))
        return len(max_sub)



    '''
    O(n^2)解法:

    Dpi 表示以第i个数字为结尾的最长上升子序列的长度。 对于每个数字, 枚举前面所有小于自己的数字 j
    Dpi = max{Dpj} + 1. 如果没有比自己小的, Dpi = 1;


    和368 Largest Divisible Subset同個模板

    '''

    def lengthOfLIS_DP(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i] 表示以第 i 个数结尾的 LIS 的长度
        # initialization: dp[0..n-1] = 1
        n = len(nums)
        dp = [1] * n
        # prev[i] 代表 dp[i] 的最优值是从哪个 dp[j] 算过来的
        prev = [-1] * n
        # function: dp[i] = max(dp[j] + 1), j < i && nums[j] < nums[i]
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
                    if dp[i] == dp[j] + 1:
                        prev[i] = j



        # answer: max(dp)
        # 這段只是找出所有元素，可有可無，除非題目要求寫出所有元素
        longest = max(dp)
        last = dp.index(longest)


        path = []
        while last != -1:
            path.append(nums[last])
            last = prev[last]

        print(path[::-1])
        return longest





nums = [10,9,2,5,3,7,101,18]
assert 4 == Solution().lengthOfLIS(nums)

nums = [7,7,7,7,7,7,7]
assert 1 == Solution().lengthOfLIS(nums)

nums = [4,10,4,3,8,9]
assert 3 == Solution().lengthOfLIS(nums)
nums = [4,10,4,3,8,9]
assert 3 == Solution().lengthOfLIS_DP(nums)