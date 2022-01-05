'''
Level: Medium

Given an input string, reverse the string word by word.

A word is defined as a sequence of non-space characters.
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words.
Do not include any extra spaces.


Example:

Input: "the sky is blue",
Output: "blue is sky the".

Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation:
You need to reduce multiple spaces between two words to a single space in the reversed string.

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces.
However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.

Follow-up:
If the string data type is mutable in your language,
can you solve it in-place with O(1) extra space?
'''



class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = []
        s = s.strip()
        tmp = s.split(" ")
        for i in range(len(tmp)):
            tmp[i].strip()
            if tmp[i] == '':
                continue
            lst.append(tmp[i])

        rtn = ""
        if lst != []:
            rtn = ''.join([lst.pop()])
        while lst != []:
            rtn = ''.join([rtn , " ", lst.pop()])
            #lst.pop()
        return rtn



    def reverseWords2(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        S = s.split(" ")
        for i in range(len(S))[::-1]:
            if S[i] == "":
                S.remove(S[i])
        ans = ' '.join(S[::-1])
        print(ans)
        return ans








s = "the sky is blue"
assert "blue is sky the" == Solution().reverseWords2(s)

s = "  hello world  "
assert "world hello" == Solution().reverseWords2(s)

s = "a good   example"
assert "example good a" == Solution().reverseWords2(s)