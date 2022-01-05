'''
Level: Medium

Given an input character array, reverse the array word by word.

A word is defined as a sequence of non-space characters.

The input character array does not contain leading or trailing spaces

and the words are always separated by a single space.

Example1

Input: s = "the sky is blue"
Output: "blue is sky the"

Example2

Input: "a b c"
Output: "c b a"

Follow-up:
Could you do it in-place without allocating extra space?

'''

class Solution:
    """
    @param str: a string
    @return: return a string
    """
    def reverseWords(self, s):
        # write your code here
        s = s.strip()
        S = s.split(" ")
        for i in range(len(S))[::-1]:
            if S[i] == "":
                S.remove(S[i])
        ans = ' '.join(S[::-1])
        print(ans)
        return ans

s = "the sky is blue"
assert "blue is sky the" == Solution().reverseWords(s)
s = "a b c"
assert "c b a" == Solution().reverseWords(s)