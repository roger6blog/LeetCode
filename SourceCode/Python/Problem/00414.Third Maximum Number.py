'''
Level: Easy

Given an integer array nums, return the third distinct maximum number in this array.

If the third maximum does not exist, return the maximum number.

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.


Constraints:

1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1


Follow up: Can you find an O(n) solution?


'''

'''
找出整個數列裡不重複  第三大的數
如果不重複的數小於三個  就找出最大的那個數
'''


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = list(set(nums))
        ans.sort()
        if len(ans) >= 3:
            return ans[-3]
        else:
            return max(ans)


nums = [2,2,3,1]
assert 1 == Solution().thirdMax(nums)

nums = [3,2,1]
assert 1 == Solution().thirdMax(nums)

nums = [1,2]
assert 2 == Solution().thirdMax(nums)

nums = [5,2,2]
assert 5 == Solution().thirdMax(nums)

nums = [1,2,2]
assert 2 == Solution().thirdMax(nums)

nums = [1,2,2,5,3,5]
assert 2 == Solution().thirdMax(nums)