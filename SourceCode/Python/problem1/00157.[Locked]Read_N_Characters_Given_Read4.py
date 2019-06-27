
'''
Level: Easy

## Read N Characters Given Read4 I

The API  

`int read4(char *buf)`

reads 4 characters at a time from a file.
The return value is the actual number of characters read.
For example,
it returns 3 if there is only 3 characters left in the file.
By using the read4 API,
implement the function `int read(char *buf, int n)` that reads n characters from the file.

>**Note**

The read function will only be called once for each test case.

'''

# Forward declaration of the read4 API.
# read4(buf)

class Solution(object):
    def read(self, buf, n):
        '''
        * @param buf Destination buffer
        * @param n   Maximum number of characters to read
        * @return    The number of characters read
        '''
        Readbyte = 0
        bufread4 = ['']*4
        while Readbyte < n:
            res = read4(bufread4)  # size maybe 4 since there is no char in file
            copyBytes = min(n, res)
            if res < 4:
                break
            Readbyte += copyBytes
            for i in xrange(res):
                buf[Readbyte + i ] = bufread4[i]
        if res < 4 or Readbyte == n:
            return Readbyte
    
