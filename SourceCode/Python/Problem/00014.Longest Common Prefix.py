'''
Level: Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.


'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]

        ans = ""
        strs.sort(key=lambda x: len(x))
        for i in range(len(strs[0])):
            substr = strs[0][:i+1]
            for other in strs[1:]:
                not_prefix = False
                for k in range(len(substr)):

                    if substr[k] != other[k]:
                        not_prefix = True
                if not_prefix:
                    break

            else:
                if len(substr) > len(ans):
                    ans = substr

        print(ans)
        return ans

    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""

        if len(strs) == 1:
            return strs.pop()

        minstr = ""
        minlen = sys.maxint
        for s in strs:
            minlen = min(minlen, len(s))
            if minlen == len(s):
                minstr = s


        ans = ""
        for i in xrange(minlen):
            for s in strs:
                if s != strs[0] and s[i] != minstr[i]:
                    return ans

            ans += minstr[i]

        return ans

strs = ["flower","flow","flight"]
assert "fl" == Solution().longestCommonPrefix(strs)

strs = ["dog","racecar","car"]
assert "" == Solution().longestCommonPrefix(strs)

strs = ["a"]
assert "a" == Solution().longestCommonPrefix(strs)

strs = ["ab", "a"]
assert "a" == Solution().longestCommonPrefix(strs)

strs = ["reflower","flow","flight"]
assert "" == Solution().longestCommonPrefix(strs)

strs = ["abca","aba","aaab"]
assert "a" == Solution().longestCommonPrefix(strs)