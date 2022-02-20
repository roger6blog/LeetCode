'''
Level: Medium   Tag: [Stack]


Given string num representing a non-negative integer num, and an integer k,

return the smallest possible integer after removing k digits from num.



Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.


Constraints:

1 <= k <= num.length <= 10^5
num consists of only digits.
num does not have any leading zeros except for the zero itself.


'''


'''

可以使用单调栈。 从高位向低位依次入栈，若当前数字小于栈顶元素且k不为0，则删除栈顶元素。 最后将栈内的元素变为数字即可。
為什麼要移除棧頂元素?  因為棧頂元素必定比當前元素高位
如果他的數字比較大  那這數字只要留著  不管後面怎麼樣處理這組成的數字都一定比他們大
所以必須移除

'''

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return num

        if k >= len(num):
            return 0

        ans = []

        for i in range(len(num)):
            while ans and k > 0 and ans[-1] > num[i]:
                ans.pop()
                k -= 1

            if num[i] != '0' or len(ans) > 0:
                ans.append(num[i])


        while ans and k > 0:
            ans.pop()
            k -= 1

        if len(ans) == 0:
            return "0"

        ans = ''.join(ans)
        return ans

num = "1432219"
k = 3
Solution().removeKdigits(num, k)