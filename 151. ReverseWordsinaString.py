

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
        
        
