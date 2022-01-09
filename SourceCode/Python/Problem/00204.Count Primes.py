'''

Given an integer n, return the number of prime numbers that are strictly less than n.



Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:

Input: n = 0
Output: 0

Example 3:

Input: n = 1
Output: 0


Constraints:

0 <= n <= 5 * 10^6

'''

class Solution(object):
    def countPrimes_TLE(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_prims(n):
            if n == 2 or n == 3:
                return True
            if n%2 == 0 or n < 2:
                return False
            for i in range(3, int(n**0.5)+1, 2):
                if n % i == 0:
                    return False
            return True

        ans = 0
        for i in range(2, n):
            if is_prims(i) == True:
                ans += 1

        print(ans)
        return ans

    '''
    埃拉托斯特尼筛法
    就是搞一个N那么大的array， 然后碰到质数， 就把后面质数所有小于n的倍数给mark一遍。

    这个方法时间复杂度是nlogn因为1/2+1/3+1/4+...+1/n根据数学知识，是趋近于lnN的
    '''
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def mark_non_prime(prime, n, nums):
            curr = prime + prime
            while curr < n:
                nums[curr] = 1
                curr += prime

        nums = [0] * n
        for i in range(2, int(n**0.5)+1):
            if nums[i] == 0:
                mark_non_prime(i, n, nums)

        if n > 2:
            ans = n - sum(nums) - 2 # we ignore 0 and 1 at begging
        else:
            ans = 0

        print(ans)
        return ans

n = 10
Solution().countPrimes(n)