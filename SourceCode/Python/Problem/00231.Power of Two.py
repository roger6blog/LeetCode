'''
Level: Easy  Tag: [Math]

Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 2^0 = 1

Example 2:

Input: 16
Output: true
Explanation: 2^4 = 16

Example 3:

Input: 218
Output: false

Constraints:

-2^31 <= n <= 2^31 - 1

Follow up: Could you solve it without loops/recursion?

'''


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        if n == 1:
            return True

        while n > 1:
            if n % 2 == 1:
                return False
            n = n / 2
        return True


    '''
    如果一个数是2的次方数的话，根据上面分析，那么它的二进数必然是最高位为1，其它都为0，
    那么如果此时我们减1的话，则最高位会降一位，其余为0的位现在都为变为1，那么我们把两数相与，就会得到0
    '''


    def isPowerOfTwo2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0 :
            return False

        if n & n-1 == 0:
            return True
        return False






print(Solution().isPowerOfTwo(16))