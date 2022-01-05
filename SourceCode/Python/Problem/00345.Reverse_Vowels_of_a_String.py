'''
Level: Easy

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

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


    def reverseVowels2(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = ["a", "i", "u", "e", "o", "A", "I", "U", "E", "O"]
        vowel_list = []
        s = list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                vowel_list.append(s[i])
                s[i] = "囧"

        for i in range(len(s)):
            if s[i] == "囧":
                s[i] = vowel_list.pop()

        s = ''.join(s)
        print(s)

        return s

    def reverseVowels_2_ptr(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = ["a", "i", "u", "e", "o", "A", "I", "U", "E", "O"]
        s = list(s)

        left = 0
        right = len(s)-1

        while left <= right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
                continue
            if s[left] not in vowels:
                left += 1
            if s[right] not in vowels:
                right -= 1

        s = ''.join(s)
        print(s)
        return s


s = "leetcode"
assert "leotcede" == Solution().reverseVowels_2_ptr(s)
s = "ai"
assert "ia" == Solution().reverseVowels_2_ptr(s)
s = "aA"
assert "Aa" == Solution().reverseVowels_2_ptr(s)
s = "!!!"
assert "!!!" == Solution().reverseVowels_2_ptr(s)