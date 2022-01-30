'''
Level: Medium   Tag: [Math]

Your task is to calculate a^b mod 1337 where a is a positive integer

and b is an extremely large positive integer given in the form of an array.


Example 1:

Input: a = 2, b = [3]
Output: 8

Example 2:

Input: a = 2, b = [1,0]
Output: 1024

Example 3:

Input: a = 1, b = [4,3,3,8,5,2]
Output: 1


Constraints:

1 <= a <= 2^31 - 1
1 <= b.length <= 2000
0 <= b[i] <= 9
b does not contain leading zeros.


'''

class Solution(object):
    def superPow_TLE(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        b = map(str, b)
        b = int("".join(b))
        ans = pow(a, b) % 1337
        print(ans)
        return ans

    '''
    这道题和之前那道Pow(x, n)的解法很类似，我们都得对半缩小，不同的是后面都要加上对1337取余。
    由于给定的指数b是一个一维数组的表示方法，我们要是折半缩小处理起来肯定十分不方便，所以我们采用按位来处理，
    比如2^23 = (2^2)^10 * 2^3, 所以我们可以从b的最高位开始，算出个结果存入res，
    然后到下一位是，res的十次方再乘以a的该位次方再对1337取余
    '''


    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        ans = 1
        for n in b:
            ans = ( pow(ans, 10) * pow(a, n) ) % 1337

        print(ans)
        return ans
a = 2
b = [4,3,3,8,5,2]
Solution().superPow(a, b)
