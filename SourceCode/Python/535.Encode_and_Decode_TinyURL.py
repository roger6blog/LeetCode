'''

Note: This is a companion problem to the System Design problem: Design TinyURL.

TinyURL is a URL shortening service
where you enter a URL such as https://leetcode.com/problems/design-tinyurl
and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service.

There is no restriction on how your encode/decode algorithm should work.

You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.


'''

import random
class Codec:
    def __init__(self):
        self.urlIndex = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """

        x = ''
        while len(x) != 6 and x not in self.urlIndex:
            for i in xrange(6):
                x += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890")
            if x not in self.urlIndex:
                self.urlIndex[x] = longUrl
        return "http://tinyurl.com/" + x

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """

        url = shortUrl.split("/")[-1]
        if url in self.urlIndex:
            return self.urlIndex[url]


url = "https://www.example.com/approval/bomb"
# Your Codec object will be instantiated and called as such:
codec = Codec()
print codec.decode(codec.encode(url))