'''
Level: Medium  Tag:[Stack]

Write a program to find the n-th super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

Input: n = 12, primes = [2,7,13,19]
Output: 32
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12
             super ugly numbers given primes = [2,7,13,19] of size 4.

Example 2:

Input: n = 1, primes = [2,3,5]
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are in the array primes = [2,3,5].


Note:

1 is a super ugly number for any given primes.
The given numbers in primes are in ascending order.
0 < k <= 100, 0 < n <= 10^6, 0 < primes[i] < 1000.
primes[i] is guaranteed to be a prime number.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.


'''
import sys
import heapq
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n <= 1:
            return 1
        ugly =[]
        factor = {}
        for _ in primes:
            factor[_] = 0

        ugly.append(1)
        for i in xrange(1, n):
            ugly.append(sys.maxint)
            for p in factor:
                ugly[i] = min(ugly[i], ugly[factor[p]] * p)

            for p in factor:
                if ugly[i] == ugly[factor[p]] * p:
                    factor[p] += 1

        return ugly[-1]



    def nthSuperUglyNumber_heapq_TLE(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ans = []
        heapq.heappush(ans, 1)
        seen = []
        curr_ugly = 1
        for _ in range(n):
            curr_ugly = heapq.heappop(ans)
            for p in primes:
                ugly = curr_ugly * p
                if ugly not in seen:
                    heapq.heappush(ans, ugly)
                    seen.append(ugly)

        print(curr_ugly)
        return curr_ugly


n = 12
primes = [2,7,13,19]

print(Solution().nthSuperUglyNumber(n, primes))
print(Solution().nthSuperUglyNumber2(n, primes))