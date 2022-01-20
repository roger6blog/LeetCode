'''
Level: Medium  Tag: [Queue], [QuickSort]

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:

1 <= k <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4


'''
from audioop import reverse
from turtle import left


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # Quick sort python version, but it will be TLE
        def quick_sort(arr):
            less = []
            equal = []
            greater = []
            if len(arr) > 1:
                pivot = arr[0]
                for x in arr:
                    if x < pivot:
                        less.append(x)
                    elif x > pivot:
                        greater.append(x)
                    else:
                        equal.append(x)
                return quick_sort(less) + equal + quick_sort(greater)

            else:
                return arr


        def quick_select(nums, k):
            l, r = 0, len(nums)
            m = nums[(l + r) // 2]
            left, mid, right = [], [], []
            for num in nums:
                if num < m:
                    left.append(num)
                elif num > m:
                    right.append(num)
                else:
                    mid.append(num)
            if len(right) >= k:
                return quick_select(right, k)
            elif len(mid) + len(right) >= k:
                return m
            else:
                return quick_select(left, k - len(mid) - len(right))
        return quick_select(nums, k)



nums = [3,2,1,5,6,4]
k = 2
assert 5 == Solution().findKthLargest(nums, k)

nums = [2,1]
k = 1
assert 5 == Solution().findKthLargest(nums, k)