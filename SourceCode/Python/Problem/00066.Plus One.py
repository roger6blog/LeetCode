'''
Level: Easy

Given a non-empty array of digits representing a non-negative integer,
plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero,
except the number 0 itself.

Increment the large integer by one and return the resulting array of digits.


Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.


Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].


Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.

'''


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(len(digits)):
            num = num + (digits[i] * (10 ** (len(digits) - i -1 ) ))
        num += 1
        return [int(x) for x in str(num)]




    def plusOne2(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = [str(d) for d in digits ]
        digits = int("".join(digits))
        digits += 1
        digits = list(str(digits))
        digits = [int(d) for d in digits ]
        print(digits)
        return digits






s = [1,3,4,2]
sol = Solution()
print(sol.plusOne(s))


s = [4,3,2,1]
Solution().plusOne2(s)