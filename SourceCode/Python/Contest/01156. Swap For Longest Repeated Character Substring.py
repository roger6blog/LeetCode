'''
1156. Swap For Longest Repeated Character Substring

Difficulty: Medium
Given a string text, we are allowed to swap two of the characters in the string. Find the length of the longest substring with repeated characters.



Example 1:

Input: text = "ababa"
Output: 3
Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa", which its length is 3.
Example 2:

Input: text = "aaabaaa"
Output: 6
Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa", which its length is 6.
Example 3:

Input: text = "aaabbaaa"
Output: 4
Example 4:

Input: text = "aaaaa"
Output: 5
Explanation: No need to swap, longest repeated character substring is "aaaaa", length is 5.
Example 5:

Input: text = "abcdef"
Output: 1


Constraints:

1 <= text.length <= 20000
text consist of lowercase English characters only.

'''

import re
class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        n = len(text)
        repeats = r'(.)\1+'
        max_str = sorted((m.group() for m in re.finditer(repeats, text)),
                            key=len, reverse=True)
        if not max_str:
            return 1
        max_str = [s for s in max_str if len(s) == len(max_str[0])]

        if len(max_str[0]) == len(text):
            return 0

        total_len = 0
        for s in max_str:
            total_len += len(s)

        if total_len == n:
            return 0
        elif total_len +1 == n:
            return total_len
        else:
            return len(max_str[0]) + 1
print(Solution().maxRepOpt1("ababa"))