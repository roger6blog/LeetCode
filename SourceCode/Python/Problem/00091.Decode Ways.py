'''
Level: Medium  Tag: DP

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways).

For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.



Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").


Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).



'''




















'''
DP[n] 為一個長度為n的字串能被數字表示的方法
則 第n位數字不能和n-1位數字一起解碼時 DP[n] = DP[n] + DP[n-1]
   第n位數字可以和n-1位數字一起解碼時 DP[n] = DP[n] + DP[n-2]

   何時第n位數字不能和n-1位數字一起解碼?
   第n-1位和n-2的數字合起來是 01~09 的時候
   何時第n位數字可以和n-1位數字一起解碼?
   第n-1位和n-2的數字合起來是 10~26 的時候

'''
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0

        dp = [0] * (n+1)

        # 初始值設定
        # 因為從2開始循環，所以要先處理1個長度字串的情況
        dp[0] = 1
        if s[0] == '0':
            dp[1] = 0
        else:
            dp[1] = 1

        for i in range(2, n+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if 26 >= int(s[i-2:i]) >= 10:
                dp[i] += dp[i-2]

        print(dp[-1])
        return dp[-1]

s = "226"
Solution().numDecodings(s)