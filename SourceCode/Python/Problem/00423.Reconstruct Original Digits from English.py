'''
Level: Medium

Given a string s containing an out-of-order English representation of digits 0-9,

return the digits in ascending order.



Example 1:

Input: s = "owoztneoer"
Output: "012"

Example 2:

Input: s = "fviefuro"
Output: "45"


Constraints:

1 <= s.length <= 10^5
s[i] is one of the characters ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"].
s is guaranteed to be valid.

'''


class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        nums = [0] * 10
        ans = ""

        nums[0] = s.count("z")
        nums[8] = s.count("g")
        nums[2] = s.count("w")
        nums[3] = s.count("h") - nums[8]
        nums[6] = s.count("x")
        nums[4] = s.count("u")
        nums[5] = s.count("f") - nums[4]
        nums[7] = s.count("s") - nums[6]
        nums[1] = s.count("o") - nums[2] - nums[4] - nums[0]
        nums[9] = (s.count("n") - nums[1] - nums[7]) // 2

        for i in range(len(nums)):
            ans += str(i) * nums[i]

        print(ans)
        return ans

s = "zerozero"
assert '00' == Solution().originalDigits(s)
s = "egith"
assert '8' == Solution().originalDigits(s)

s = "fviefuro"
assert '45' == Solution().originalDigits(s)
s = "owoztneoer"
assert '012' == Solution().originalDigits(s)
