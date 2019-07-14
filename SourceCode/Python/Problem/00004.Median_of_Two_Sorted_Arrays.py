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
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merge_lst = []
        while nums1 or nums2:
            if not nums1:
                merge_lst.extend(nums2)
                nums2 = []
                break
            elif not nums2:
                merge_lst.extend(nums1)
                nums1 = []
                break

            if nums1[0] <= nums2[0]:
                merge_lst.append(nums1[0])
                if len(nums1) >= 1:
                    nums1 = nums1[1:]
                else:
                    nums1 = []
            else:
                merge_lst.append(nums2[0])

                if len(nums2) >= 1:
                    nums2 = nums2[1:]
                else:
                    nums2 = []




        n = len(merge_lst)
        if n % 2 == 0:
            median = float(merge_lst[n/2 - 1] + merge_lst[n/2]) / 2.0
        else:
            median = float(merge_lst[n/2])

        return median

    def findMedianSortedArrays_Rec(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def getKth(A, B, k):
            lenA = len(A)
            lenB = len(B)

            # Make length of A always smaller than B
            if lenA > lenB:
                return getKth(B, A, k)

            # min(k/2, lenA)-1 will lead lenA == 0,
            # so add this checking
            if lenA == 0:
                return B[k - 1]
            # min(k/2, lenA)-1 will lead k == 1,
            # so add this checking
            if k == 1:
                return min(A[0], B[0])

            pa = min(k / 2, lenA)
            pb = k - pa
            if A[pa - 1] <= B[pb - 1]:
                return getKth(A[pa:], B, pb)
            else:
                return getKth(A, B[pb:], pa)
        lenA = len(nums1)
        lenB = len(nums2)
        if (lenA + lenB) % 2 == 1:
            return getKth(nums1, nums2, (lenA + lenB)/2 + 1)
        else:
            return (getKth(nums1, nums2, (lenA + lenB)/2) + \
                    getKth(nums1, nums2, (lenA + lenB)/2 + 1)) / 2.0


nums1 = [1, 3, 5, 7]
nums2 = [2, 4, 6, 8, 9, 10]

print Solution().findMedianSortedArrays(nums1, nums2)