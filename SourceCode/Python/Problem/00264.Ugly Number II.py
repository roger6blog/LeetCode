'''
Level: Medium  Tag: [Math]

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.

'''
import heapq

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly =[]
        p2 = 0
        p3 = 0
        p5 = 0
        ugly.append(1)
        for i in xrange(1, n):
            ugly.append(0)
            ugly[i] = min(ugly[p2]*2, ugly[p3]*3, ugly[p5]*5)
            if ugly[i] == ugly[p2] * 2:
                p2 += 1
            if ugly[i] == ugly[p3] * 3:
                p3 += 1
            if ugly[i] == ugly[p5] * 5:
                p5 += 1

        return ugly[-1]

    '''
    创建最小堆heap，哈希表 seen和质因数列表factors = [2, 3, 5]。heap用于存储已生成的丑数，弹出最小值；seen用于标记堆中出现过的元素，避免重复入堆。
    初始化将1入堆，并添加到seen。
    重复以下步骤n次: 弹出堆中最小的数字 curr_ugly。
        对于factors中每个因数f，生成新的丑数ugly。若ugly不在seen中，则将其添加到heap中并更新seen。
    curr_ugly即为第n小的丑数，返回。
    '''

    def nthUglyNumber2(self, n):
        """
        :type n: int
        :rtype: int
        """

        heap = []
        heapq.heappush(heap, 1)
        prime = [2, 3, 5]
        seen = []
        curr_ugly = 0
        for _ in range(n):
            curr_ugly = heapq.heappop(heap)
            for p in prime:
                ugly = curr_ugly * p
                if ugly not in seen:
                    heapq.heappush(heap, ugly)
                    seen.append(ugly)

        print(curr_ugly)
        return curr_ugly


n = 100
print(Solution().nthUglyNumber(n))
print(Solution().nthUglyNumber2(n))