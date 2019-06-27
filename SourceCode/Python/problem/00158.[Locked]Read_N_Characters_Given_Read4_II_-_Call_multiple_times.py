
'''
Level: Hard Tag:[]
(Continue with 152
Read N Characters Given Read4 II - Call multiple times
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note: The read function may be called multiple times.

'''

class Solution(object):
    '''算法思路：
    將每次讀取buf後剩餘的部分儲存起來
    '''
    def __init__(self):
        self.left = []

    def read(self, buf, n):
        count, reads = 0, [''] * 4

        if self.left:
            while count < min(len(self.left), n):
                buf[count] = self.left[count]
                count += 1
            self.left = self.left[count:]

        while count < n:
            size = read4(reads)
            if not size:
                break
            surplus = min(n - count, size)
            self.left.append(reads[surplus:size])
            #self.left = reads[surplus:size]
            #for i in xrange(surplus):
            for i in xrange(size - surplus):
                buf[count] = reads[i]
                count += 1
        return count

    
index = 0
string = 'abcdefg'

def read4(reads):
    global index

    count = 0
    while count < 4 and index < len(string):
        reads[count] = string[index]
        count += 1
        index += 1
    return count


s = Solution()
buf = [0] * 100
print s.read(buf, 3)
print s.read(buf, 4)
print s.read(buf, 3)
            
