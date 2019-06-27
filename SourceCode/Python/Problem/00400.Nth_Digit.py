'''

Find the nth digit of the infinite integer sequence

1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 2^31).

Example 1:

Input:
3

Output:
3

Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0,

which is part of the number 10.

'''


class Solution_TLE(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        i = len(str(n))

        j = i*(10**i)*9
        numlist = ''
        for x in xrange(j):
            numlist += str(x)
        return int(numlist[n:n+1])


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = n
        for i in xrange(10):
            domain = 9 * (10**i)              # i is digit of answer, 0~9
            if n <= domain * (i + 1):
                break
            print("{} digit has {} length number".format(i+1, domain * (i + 1)))
            print("{} - {} = {}".format(n, domain * (i + 1), n - domain * (i + 1)))
            n-= domain * (i + 1)  # Look up over number, if n = 11,
                                  # over number is 11 - 9 = 2

        print("n is in {} digits range").format(i+1)
        n -= 1 # n = 2 - 1 = 1
        x = 10**i + n / (i + 1) # Look up first number in domain
        print("{} is in {} number".format(m, x))
        ans = str(x)[n%(i+1)]
        print("{}th number is {}".format(m, ans))
        return int(ans)

print Solution().findNthDigit(1234)