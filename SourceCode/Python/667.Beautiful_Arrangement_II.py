'''

Given two integers n and k,

you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement:

Suppose this list is [a1, a2, a3, ... , an],

then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.

Example 1:
Input: n = 3, k = 1
Output: [1, 2, 3]
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.

Example 2:
Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.

Note:
The n and k are in the range 1 <= k < n <= 10^4.


'''
class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        left = 1
        right = n
        ans = []
        while left <= right:
            if k > 1:
                if k % 2 == 1:
                    ans.append(left)
                    left += 1
                else:
                    ans.append(right)
                    right -= 1
            else:
                ans.append(left)
                left += 1
            k -= 1
        return ans




class Solution_TLE(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """

        nums = []
        ans = []
        for i in xrange(n):
            nums.append(i+1)

        self.exhaustive(nums, 0, ans, k)
        return ans.pop()
    def exhaustive(self, nums, index, ans, k):
        if index >= len(nums):
            temp = []
            for i in xrange(len(nums)-1):
                temp.append(abs(nums[i+1] - nums[i]))
            if len(set(temp)) == k:
                ans.append(nums[:])
            return
        else:
            for i in xrange(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                self.exhaustive(nums, index+1, ans, k)
                if len(ans) != 0:
                    return
                nums[index], nums[i] = nums[i], nums[index]


n = 90
k = 82

print Solution().constructArray(n, k)