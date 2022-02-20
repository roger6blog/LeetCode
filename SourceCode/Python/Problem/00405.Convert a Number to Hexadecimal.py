'''
Level: Easy  Tag: [Math]

Given an integer num, return a string representing its hexadecimal representation.

For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters,

and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.



Example 1:

Input: num = 26
Output: "1a"

Example 2:

Input: num = -1
Output: "ffffffff"


Constraints:

-2^31 <= num <= 2^31 - 1


'''

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'

        hex_map = {
            10: 'a',
            11: 'b',
            12: 'c',
            13: 'd',
            14: 'e',
            15: 'f'
            }
        ans = ''
        if num < 0:
            num += 2**32

        while num >= 16:
            if num % 16 < 10:
                ans = str(num % 16) + ans
            else:
                ans = hex_map[num % 16] + ans
            num = num // 16

        if num < 10:
            ans = str(num) + ans
        else:
            ans = hex_map[num] + ans


        print(ans)
        return ans
num = 26
assert '1a' == Solution().toHex(num)

num = 999
assert '3e7' == Solution().toHex(num)

num = -1
assert 'ffffffff' == Solution().toHex(num)

num = 16
Solution().toHex(num)
