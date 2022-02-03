'''
Level: Medium  Tag: [Math]

You are given an integer array nums of length n.

Assume arr(k) to be an array obtained by rotating nums by k positions clock-wise.

We define the rotation function F on nums as follow:

F(k) = 0 * arr(k)[0] + 1 * arr(k)[1] + ... + (n - 1) * arr(k)[n - 1].
Return the maximum value of F(0), F(1), ..., F(n-1).

The test cases are generated so that the answer fits in a 32-bit integer.


Example 1:

Input: nums = [4,3,2,6]
Output: 26
Explanation:
F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.

Example 2:

Input: nums = [100]
Output: 0


Constraints:

n == nums.length
1 <= n <= 10^5
-100 <= nums[i] <= 100

'''

class Solution(object):
    def maxRotateFunction_TLE(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        n = len(nums)
        if n == 1:
            return 0

        nn = nums
        for _ in range(n):
            res = 0
            for i in range(n):
                res += nn[i] * i
            ans = max(ans, res)
            nn = nn[1:] + nn[:1]

        print(ans)

        return ans



    '''
    我们为了找规律，先把具体的数字抽象为A,B,C,D，那么我们可以得到:

    F(0) = 0A + 1B + 2C +3D

    F(1) = 0D + 1A + 2B +3C

    F(2) = 0C + 1D + 2A +3B

    F(3) = 0B + 1C + 2D +3A

    那么，我们通过仔细观察，我们可以得出下面的规律:

    sum = 1A + 1B + 1C + 1D

    F(1) = F(0) + sum - 4D

    F(2) = F(1) + sum - 4C

    F(3) = F(2) + sum - 4B

    那么我们就找到规律了, F(i) = F(i-1) + sum - n*A[n-i]

    '''

    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)  # 必須先算好  不然會TLE
        n = len(nums)
        f = [0] * n

        for i in range(n):
            f[0] += i*nums[i]

        ans = f[0]

        for i in range(1, n):
            f[i] = f[i-1] + s - n*nums[n-i]
            ans = max(ans, f[i])

        print(ans)

        return ans

nums = [4,3,2,6]
Solution().maxRotateFunction(nums)