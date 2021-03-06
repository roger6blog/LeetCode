
'''

Given an input string, reverse the string word by word.

Example:  

Input: "the sky is blue",
Output: "blue is sky the".
Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces.
However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
Follow up: For C programmers,
try to solve it in-place in O(1) space.

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
        for i in xrange(len(tmp)):
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
        
s = "the sky is blue"
print Solution().reverseWords(s)
