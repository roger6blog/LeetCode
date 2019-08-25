'''

1144. Decrease Elements To Make Array Zigzag

Difficulty: Easy
Given an array nums of integers, a move consists of choosing any element and decreasing it by 1.

An array A is a zigzag array if either:

Every even-indexed element is greater than adjacent elements, ie. A[0] > A[1] < A[2] > A[3] < A[4] > ...
OR, every odd-indexed element is greater than adjacent elements, ie. A[0] < A[1] > A[2] < A[3] > A[4] < ...
Return the minimum number of moves to transform the given array nums into a zigzag array.



Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation: We can decrease 2 to 0 or 3 to 1.
Example 2:

Input: nums = [9,6,1,6,2]
Output: 4


Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 1000


'''


class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def isZigZag(prev, curr, next):
            return ((prev < curr and next < curr)  or (prev > curr and next > curr))


        res = True
        for i in range(1, len(nums)-1):
            if not isZigZag(nums[i-1], nums[i], nums[i+1]):
                res = False

        if res:
            return 0

        ans_1 = 0
        ans_2 = 0
        ans_3 = 0
        ans_4 = 0
        n = len(nums)
        if n == 1:
            return 0
        for i in range(0, n-1, 2):
            if i == 0 and nums[0] >= nums[1]:
                ans_1 += nums[0] - nums[1] + 1

            else:
                if i != 0:
                    mi = nums[i-1]
                    if i != n-1:
                        mi = min(mi, nums[i+1])

                    if nums[i] <= mi:
                        ans_1 += mi - nums[i] + 1

            if i == 0 and nums[i] <= nums[i+1]:
                ans_2 += nums[i+1] - nums[i] + 1
            else:
                if i != 0:
                    ma = nums[i-1]
                    if i != n-1:
                        ma = max(ma, nums[i+1])
                    if nums[i] >= ma:
                        ans_2 += nums[i] - ma + 1


        return min(ans_1, ans_2)





nums = [1,2,3]
nums2 = [9,6,1,6,2]
nums3 = [1,2,1,3]
nums4 = [2,7,10,9,8,9]
print Solution().movesToMakeZigzag(nums4)