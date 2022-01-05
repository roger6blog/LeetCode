'''
Leave: Medium

Design an algorithm to encode a list of strings to a string.

The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) { // ... your code return encoded_string; }

Machine 2 (receiver) has the function:

vector<string> decode(string s) { //... your code return strs; }

So Machine 1 does: string encoded_string = encode(strs);

and Machine 2 does: vector<string> strs2 = decode(encoded_string);

strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"

Note:

The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters. Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless. Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.


'''

'''
这道题让我们给字符加码再解码，先有码再无码，然后题目中并没有限制加码的方法，
那么只要能成功的把有码变成无码就行了，具体变换方法自己可以设计。

由于需要把一个字符串集变成一个字符串，然后把这个字符串再还原成原来的字符串集，
最开始博主想能不能在每一个字符串中间加个空格把它们连起来，然后再按空格来隔开，
但是这种方法的问题是原来的一个字符串中如果含有空格，那么还原的时候就会被分隔成两个字符串，所以必须还要加上长度的信息，
加码方法是长度 + "/" + 字符串，比如对于 "a","ab","abc"，就变成 "1/a2/ab3/abc"，
那么解码的时候就有规律可寻，先寻找 "/"，然后之前的就是要取出的字符个数，从 "/" 后取出相应个数即可，
以此类推直至没有 "/"了，这样就得到高清无码的字符串集了

'''



class Solution:
    def encode(self, strs):
        """
        @param: strs: a list of strings
        @return: encodes a list of strings to a single string.
        """
        encode_str = []
        for word in strs:
            for w in word:
                encode_str.append("{}-".format(ord(w)))
            encode_str.append(":")
        encode_str[-1] = "!"
        encode_str = "".join(encode_str)

        return encode_str



    def decode(self, strs):
        """
        @param: strs: a list of strings
        @return: encodes a list of strings to a single string.
        """
        t = strs[:-1].split(":")
        decode_str = []
        for words in t:
            curr = ""
            word_lst = words[:-1].split("-")
            for c in word_lst:
                curr += chr(int(c))
            decode_str.append(curr)

        return decode_str

s = ["lint","code","love","you"]
print(Solution().encode(s))
t = "108-105-110-116-:99-111-100-101-:108-111-118-101-:121-111-117-!"
print(Solution().decode(t))