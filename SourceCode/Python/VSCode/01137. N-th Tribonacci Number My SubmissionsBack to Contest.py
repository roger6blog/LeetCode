'''
1137. N-th Tribonacci Number My SubmissionsBack to Contest

Difficulty: Easy
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.



Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537


Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

'''

class Solution(object):
    def __init__(self):
        self.dp_table = [0] * 40
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 0

        if n == 2 or n == 1:
            return 1

        if self.dp_table[n] != 0:
            return self.dp_table[n]
        ans = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        self.dp_table[n] = ans
        return ans

print Solution().tribonacci(4)


