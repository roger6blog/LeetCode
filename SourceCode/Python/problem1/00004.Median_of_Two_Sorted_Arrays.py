'''

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5


'''


class Solution(object):
    def getKth(self, A, B, k):
        lenA = len(A)
        lenB = len(B)

        # Make length of A always smaller than B
        if lenA > lenB:
            return self.getKth(B, A, k)

        # min(k/2, lenA)-1 will lead lenA == 0,
        # so add this checking
        if lenA == 0:
            return B[k - 1]
        # min(k/2, lenA)-1 will lead k == 1,
        # so add this checking
        if k == 1:
            return min(A[0], B[0])

        pa = min(k/2, lenA)
        pb = k - pa
        if A[pa - 1] <= B[pb - 1]:
            return self.getKth(A[pa:], B, pb)
        else:
            return self.getKth(A, B[pb:], pa)
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lenA = len(nums1)
        lenB = len(nums2)
        if (lenA + lenB) % 2 == 1:
            return self.getKth(nums1, nums2, (lenA + lenB)/2 + 1)
        else:
            return (self.getKth(nums1, nums2, (lenA + lenB)/2) + \
                    self.getKth(nums1, nums2, (lenA + lenB)/2 + 1)) / 2.0


nums1 = [1, 3, 5, 7]
nums2 = [2, 4, 6, 8, 9, 10]

print Solution().findMedianSortedArrays(nums1, nums2)