'''
Level: Medium   Tag: [Backtrack]

A valid IP address consists of exactly four integers separated by single dots.

Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses,
but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

Given a string s containing only digits,

return all possible valid IP addresses that can be formed by inserting dots into s.

You are not allowed to reorder or remove any digits in s.

You may return the valid IP addresses in any order.



Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


Constraints:

0 <= s.length <= 20
s consists of digits only.

'''

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        ans = []
        def valid_ip(ip):
            if len(ip) == 0:
                return False
            if len(ip) > 1 and ip[0] == "0":
                return False

            if int(ip) > 255:
                return False

            return True
        def rec(index, curr, s):
            if curr.count(".") > 4:
                return

            if curr.count(".") == 4 and s == "":
                for ip in curr[1:].split("."):
                    if not valid_ip(ip):
                        return
                x = curr[1:]
                if x not in ans:
                    ans.append(x)
                return

            for i in range(1, 4):
                if i <= len(s):
                    if int(s[:i]) <= 255:
                        rec(index+1, curr+"."+s[:i], s[i:])
                    if s[0] == 0:
                        break

        rec(0, "", s)
        print(ans)
        return ans


s = "25525511135"
Solution().restoreIpAddresses(s)