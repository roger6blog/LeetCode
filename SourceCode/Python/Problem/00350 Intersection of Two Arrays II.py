'''
Level:Easy

Given two integer arrays nums1 and nums2, return an array of their intersection.

Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.



Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.


Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000


Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

'''

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1

        ans = []

        for n in nums2:
            if n in nums1:
                ans.append(n)
                nums1.remove(n)

        print(ans)
        return ans

nums1 = [1,2,2,1]
nums2 = [2,2]
assert [2, 2] == Solution().intersect(nums1, nums2)

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
assert [4,9] == Solution().intersect(nums1, nums2)

nums1 = [1,2]
nums2 = [1,1]
assert [1] == Solution().intersect(nums1, nums2)