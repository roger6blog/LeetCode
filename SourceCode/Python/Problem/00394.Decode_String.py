'''
Level: Medium  Tag: [Stack]

Given an encoded string, return it's decoded string.

The encoding rule is:

k[encoded_string],
where the encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid;

No extra white spaces, square brackets are well-formed, etc.

Furthermore,

you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.

For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].

'''

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [["", 1]]
        nums = ""
        for c in s:
            if c.isdigit():
                nums += c
            elif c == "[":
                stack.append(["", int(nums)])
                nums = ""
            elif c == "]":
                chars, k = stack.pop()
                stack[-1][0] += chars * k
            else:
                stack[-1][0] += c

        return stack[0][0]



    def decodeString2(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        stack = [["", 1]]
        for i in s:
            if i.isdigit():
                ans += i
            elif i == "[":
                stack.append(["", int(ans)])
                ans = ""
            elif i == "]":
                char, num = stack.pop()
                stack[-1][0] += num * char
            else:
                stack[-1][0] += i

        return stack[0][0]


s = "3[a2[c]]"
print Solution().decodeString2(s)