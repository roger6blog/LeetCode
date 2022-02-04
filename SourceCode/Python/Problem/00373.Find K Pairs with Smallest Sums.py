'''
Level: Medium  Tag: [Stack]

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.



Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence:
    [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]


Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence:
    [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]


Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]


Constraints:

1 <= nums1.length, nums2.length <= 10^5
-10^9 <= nums1[i], nums2[i] <= 10^9
nums1 and nums2 both are sorted in ascending order.
1 <= k <= 1000

'''
import heapq
class Solution(object):

    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        n1 = len(nums1)
        n2 = len(nums2)
        heap = []
        seen = [(0,0)]
        heapq.heappush(heap, [nums1[0]+nums2[0], 0, 0])
        ans = []
        for i in range(min(k, n1*n2)):
            _, index1, index2 = heapq.heappop(heap)
            ans.append([nums1[index1], nums2[index2]])
            if index1 < n1-1 and (index1+1, index2) not in seen:
                heapq.heappush(heap, [nums1[index1+1]+nums2[index2], index1+1, index2])
                seen.append((index1+1, index2))
            if index2 < n2-1 and (index1, index2+1) not in seen:
                heapq.heappush(heap, [nums1[index1]+nums2[index2+1], index1, index2+1])
                seen.append((index1, index2+1))

        print(ans)
        return ans

    def kSmallestPairs_TLE(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for n1 in nums1:
            for n2 in nums2:
                # push n1+n2 為了算出最小和list
                heapq.heappush(heap, [n1+n2, n1, n2])

        ans = []
        for _ in range(min(k, len(nums1)*len(nums2))):
            ans.append(heapq.heappop(heap)[1:])

        print(ans)
        return ans


nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
Solution().kSmallestPairs(nums1, nums2, k)

# nums1 = [1,2]
# nums2 = [3]
# k = 3
# Solution().kSmallestPairs(nums1, nums2, k)


nums1 = [1,2,4,5,6]
nums2 = [3,5,7,9]
k = 3
Solution().kSmallestPairs_TLE(nums1, nums2, k)
