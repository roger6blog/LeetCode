
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
        
