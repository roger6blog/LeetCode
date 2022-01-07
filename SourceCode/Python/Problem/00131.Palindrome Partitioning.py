'''
Level: Medium

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.



Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]


Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.


'''


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def backtrack(res, path, index, s):
            if len(s) == index:
                res.append(path[:])
                return

            for i in range(index, len(s)):
                substr = s[index:i+1]
                if substr == substr[::-1]:
                    path.append(substr)
                    backtrack(res, path, i+1, s)
                    path.pop()

        ans = []
        backtrack(ans, [], 0, s)

        print(ans)

        return ans



    def partition_wrong_answer(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def get_palindrome(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left+1 : right]


        ans = [list(s)]
        palin = []

        for i in range(len(s)):
            odd = get_palindrome(s, i, i)
            if len(odd) > 1 :
                palin.append(odd)
            even = get_palindrome(s, i, i+1)
            if len(even) > 1:
                palin.append(even)

        for p in palin:
            sub_strs = s.partition(p)
            sub_strs = [x for x in sub_strs if len(x)]
            if sub_strs not in ans:
                ans.append(sub_strs)
            if "".join(sub_strs) == "".join(sub_strs[::-1]) and sub_strs[::-1] not in ans:
                ans.append(sub_strs[::-1])

        print(ans)
        return ans



s = "aab"
Solution().partition(s)
s = "fff"
Solution().partition(s)
s = "abbab"
expect = [["a","b","b","a","b"],["a","b","bab"],["a","bb","a","b"],["abba","b"]]
Solution().partition(s)