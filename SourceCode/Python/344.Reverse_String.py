'''

Write a function that takes a string as input and returns the string reversed.

Example 1:

Input: "hello"
Output: "olleh"

Example 2:

Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"


'''

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "" or s == " ":
            return s

        t = s.split(" ")
        ans = ""
        if len(t) == 1:
            return s[::-1]

        while t:
            ans += t.pop()[::-1]
            if len(t) != 0:
                ans += " "

        return ans

s = "a a"
# s= "A man, a plan, a canal: Panama"
print Solution().reverseString(s)