'''
Level: Medium  Tag: DP


You are a professional robber planning to rob houses along a street.

Each house has a certain amount of money stashed.

All houses at this place are arranged in a circle.

That means the first house is the neighbor of the last one.

Meanwhile, adjacent houses have a security system connected,

and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,

return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
because they are adjacent houses.

Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:

Input: nums = [1,2,3]
Output: 3


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000

'''





'''

和198題類似的思路
但是因為建築物在此題呈現環狀
搶第一家的同時就不可能搶最後一家了
比較簡單的方法是沿用前一題的DP轉移方程式
但是計算時分成兩種情況:
1. 扣掉第一家不算
2. 扣掉最後一家不算
分別用兩個dp矩陣來計算後，找出這兩個矩陣的最後一個元素的最大值即為所求

'''




class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        if m == 0:
            return 0
        if m == 1:
            return nums[0]
        if m == 2:
            return max(nums[0], nums[1])

        dp_no_1st = [[0] * 2 for _ in range(m)]
        dp_no_last = [[0] * 2 for _ in range(m)]

        #初始值設定，因為dp_no_1st不搶第一家，所以初始值應設為第二家開始
        dp_no_1st[0][1] = nums[0]
        dp_no_1st[1][1] = nums[1]
        dp_no_last[0][1] = nums[0]

        for i in range(2, m):
            dp_no_1st[i][0] = max(dp_no_1st[i-1][0], dp_no_1st[i-1][1])
            dp_no_1st[i][1] = dp_no_1st[i-1][0] + nums[i]

        for i in range(1, m-1):
            dp_no_last[i][0] = max(dp_no_last[i-1][0], dp_no_last[i-1][1])
            dp_no_last[i][1] = dp_no_last[i-1][0] + nums[i]

        ans = max(dp_no_1st[m-1][0], dp_no_1st[m-1][1], dp_no_last[m-2][0], dp_no_last[m-2][1])

        print(ans)

        return ans


nums = [2,3,2]
assert 3 == Solution().rob(nums)

nums = [1,2,3,1]
assert 4 == Solution().rob(nums)

nums = [1,2,3]
assert 3 == Solution().rob(nums)

nums = [1,2,1,1]
Solution().rob(nums)

nums = [0]
Solution().rob(nums)