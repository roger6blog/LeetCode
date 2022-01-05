'''
Level: Easy

Write a function that takes a string as input and returns the string reversed.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]



Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.

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



    def reverseString_in_place(self, s):
        """
        :type s: str
        :rtype: str
        """
        s[:] = s[::-1]
        return s


s = ["h","e","l","l","o"]
assert ["o","l","l","e","h"] == Solution().reverseString_in_place(s)
s = ["H","a","n","n","a","h"]
assert ["h","a","n","n","a","H"] == Solution().reverseString_in_place(s)