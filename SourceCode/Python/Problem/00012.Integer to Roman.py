'''
Level: Medium

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII,
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.



Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.

Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:

1 <= num <= 3999


'''

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        from collections import OrderedDict

        roman_map = OrderedDict()

        roman_map[1000] = "M"
        roman_map[900] = "CM"
        roman_map[500] = "D"
        roman_map[400] = "CD"
        roman_map[100] = "C"
        roman_map[90] = "XC"
        roman_map[50] = "L"
        roman_map[40] = "XL"
        roman_map[10] = "X"
        roman_map[9] = "IX"
        roman_map[5] = "V"
        roman_map[4] = "IV"
        roman_map[1] = "I"

        ans = []
        for n, r in roman_map.items():
            while num >= n:
                ans.append(r)
                num -= n

        ans = "".join(ans)
        print(ans)

        return ans


num = 3
assert "III" == Solution().intToRoman(num)

num = 58
assert "LVIII" == Solution().intToRoman(num)

num = 1994
assert "MCMXCIV" == Solution().intToRoman(num)