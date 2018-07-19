'''

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

'''


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''

        vowelsTable = ['a', 'A', 'i', 'I', 'e', 'E', 'o', 'O', 'u', 'U']
        temp = []
        ans = []
        vowels = []
        for i in xrange(len(s)):
            if s[i] in vowelsTable:
                x = '~'
                vowels.append(s[i])
            else:
                x = s[i]
            temp.append(x)

        for i in temp:
            if i == '~':
                ans.append(vowels.pop())
            else:
                ans.append(i)

        return ''.join(ans)


s = "leetcode"
print Solution().reverseVowels(s)
