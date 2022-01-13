'''
Level: Medium  Tag: 2DP

You are a professional robber planning to rob houses along a street.

Each house has a certain amount of money stashed,

the only constraint stopping you from robbing each of them is that adjacent houses

have security systems connected and it will automatically contact the police

if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,

return the maximum amount of money you can rob tonight without alerting the police.


Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400

'''



'''
由抢房屋的性质可以看出，抢前m个房屋能得到的最大值，与后面如何抢的方案无关，只与前m - 1个房屋的最优方案有关。
这满足了动态规划的无后效性和最优子结构

假設DP[m][n] 為可能搶第m家所能拿到的最大金錢，n為搶這家(n=1)或不搶(n=0)
今天假設一個搶匪他搶了第m家，那他很明顯不能搶m-1家以免觸動警報
這時候的搶前m家為DP[m][0]，但是因為沒搶第m家，所以DP[m][0]為前m-1家所搶到的最大金錢DP[m-1][1]
但是也有可能第m-1家我們也沒搶啊？ 所以實際上的DP[m][0]等於DP[m-1][0]和DP[m-1][1]的最大值
如果今天我們搶了第m家，此時DP應為DP[m][1]．因為我們搶了第m家，表示我們必定沒有搶第m-1家
所以此時的DP[m][1]應該等於DP[m-1][0] 加上第m家所搶到的金錢，也就是num[m]
所以狀態轉移方程式有兩個:
DP[m][0] = max(DP[m-1][0], DP[m-1][1]
DP[m][1] = DP[m-1][0] + nums[i]
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

        dp = [[0 for _ in range(2)] for _ in range(m)]

        #定義初始條件
        dp[0][1] = nums[0]

        for i in range(1, m):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + nums[i]

        ans = max(dp[m-1][0], dp[m-1][1])
        print(ans)

        return ans

nums = [2,7,9,3,1]
assert 12 == Solution().rob(nums)

nums = [1,2,3,1]
assert 4 == Solution().rob(nums)
