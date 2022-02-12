'''
Level: Medium

Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.



Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
with the number of occurrence being 4, 3, 2 and 1 respectively.


Constraints:

1 <= words.length <= 500
1 <= words[i] <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]


'''

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        from collections import Counter
        c = Counter(words)
        ans = []
        common = c.most_common()
        most = 0
        freq = common[:]
        left = 0
        right = 0
        for word, cnt in freq:
            if most == 0:
                most = cnt
            else:
                if cnt != most:
                    ans = ans[:left] + sorted(ans[left:right])
                    most = cnt
                    left = right
            ans.append(common.pop(0)[0])
            right += 1
        else:
            ans = ans[:left] + sorted(ans[left:right])

        if left == 0:
            ans.sort()
        print(ans[:k])
        return ans[:k]

# words = ["i","love","leetcode","i","love","coding"]
# k = 1

# words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
# k = 4
# Solution().topKFrequent(words, k)

# words = ["aaa","aa","a"]
# k = 1
# Solution().topKFrequent(words, k)

# words = ["plpaboutit","jnoqzdute","sfvkdqf","mjc","nkpllqzjzp","foqqenbey","ssnanizsav","nkpllqzjzp","sfvkdqf","isnjmy","pnqsz","hhqpvvt","fvvdtpnzx","jkqonvenhx","cyxwlef","hhqpvvt","fvvdtpnzx","plpaboutit","sfvkdqf","mjc","fvvdtpnzx","bwumsj","foqqenbey","isnjmy","nkpllqzjzp","hhqpvvt","foqqenbey","fvvdtpnzx","bwumsj","hhqpvvt","fvvdtpnzx","jkqonvenhx","jnoqzdute","foqqenbey","jnoqzdute","foqqenbey","hhqpvvt","ssnanizsav","mjc","foqqenbey","bwumsj","ssnanizsav","fvvdtpnzx","nkpllqzjzp","jkqonvenhx","hhqpvvt","mjc","isnjmy","bwumsj","pnqsz","hhqpvvt","nkpllqzjzp","jnoqzdute","pnqsz","nkpllqzjzp","jnoqzdute","foqqenbey","nkpllqzjzp","hhqpvvt","fvvdtpnzx","plpaboutit","jnoqzdute","sfvkdqf","fvvdtpnzx","jkqonvenhx","jnoqzdute","nkpllqzjzp","jnoqzdute","fvvdtpnzx","jkqonvenhx","hhqpvvt","isnjmy","jkqonvenhx","ssnanizsav","jnoqzdute","jkqonvenhx","fvvdtpnzx","hhqpvvt","bwumsj","nkpllqzjzp","bwumsj","jkqonvenhx","jnoqzdute","pnqsz","foqqenbey","sfvkdqf","sfvkdqf"]
# k = 1
# Solution().topKFrequent(words, k)

# words = ["glarko","zlfiwwb","nsfspyox","pwqvwmlgri","qggx","qrkgmliewc","zskaqzwo","zskaqzwo","ijy","htpvnmozay","jqrlad","ccjel","qrkgmliewc","qkjzgws","fqizrrnmif","jqrlad","nbuorw","qrkgmliewc","htpvnmozay","nftk","glarko","hdemkfr","axyak","hdemkfr","nsfspyox","nsfspyox","qrkgmliewc","nftk","nftk","ccjel","qrkgmliewc","ocgjsu","ijy","glarko","nbuorw","nsfspyox","qkjzgws","qkjzgws","fqizrrnmif","pwqvwmlgri","nftk","qrkgmliewc","jqrlad","nftk","zskaqzwo","glarko","nsfspyox","zlfiwwb","hwlvqgkdbo","htpvnmozay","nsfspyox","zskaqzwo","htpvnmozay","zskaqzwo","nbuorw","qkjzgws","zlfiwwb","pwqvwmlgri","zskaqzwo","qengse","glarko","qkjzgws","pwqvwmlgri","fqizrrnmif","nbuorw","nftk","ijy","hdemkfr","nftk","qkjzgws","jqrlad","nftk","ccjel","qggx","ijy","qengse","nftk","htpvnmozay","qengse","eonrg","qengse","fqizrrnmif","hwlvqgkdbo","qengse","qengse","qggx","qkjzgws","qggx","pwqvwmlgri","htpvnmozay","qrkgmliewc","qengse","fqizrrnmif","qkjzgws","qengse","nftk","htpvnmozay","qggx","zlfiwwb","bwp","ocgjsu","qrkgmliewc","ccjel","hdemkfr","nsfspyox","hdemkfr","qggx","zlfiwwb","nsfspyox","ijy","qkjzgws","fqizrrnmif","qkjzgws","qrkgmliewc","glarko","hdemkfr","pwqvwmlgri"]
# k = 14
# Solution().topKFrequent(words, k)


words =["rmrypv","zgsedk","jlmetsplg","wnfbo","hnnftqf","bxlr","sviavwoxss","jdbgvc","zddeno","rxgw","hnnftqf","hdmvplne","rlmdt","jlmetsplg","ous","rmrypv","fwxulnpit","dmhuq","rxgw","ledleb","bxlr","indbvb","ckqqibnx","cub","ijww","ehd","hfhlfqzkcn","sviavwoxss","rxgw","bxjxpfp","mgqj","oic","ptk","fwxulnpit","ijww","sviavwoxss","bgfvfa","zfkgsudxq","alkq","dmhuq","zddeno","rxgw","zgsedk","amarxpg","bgfvfa","wnfbo","sviavwoxss","sviavwoxss","alkq","nmclxk","zgsedk","bwowfvira","ous","bxlr","zddeno","rxgw","ous","wnfbo","rmrypv","sviavwoxss","ehd","zgsedk","jlmetsplg","abxvhyehv","ledleb","wnfbo","bgfvfa","bwowfvira","amarxpg","wnfbo","bwowfvira","dmhuq","ouy","bxlr","rxgw","oic","hnnftqf","ledleb","rlmdt","oldainprua","ous","ckqqibnx","dmhuq","hnnftqf","oic","jlmetsplg","ppn","amarxpg","jlgfgwb","bxlr","bwowfvira","hdmvplne","oic","ledleb","bwowfvira","oic","ptk","dmhuq","abxvhyehv","ckqqibnx","indbvb","ypzfk","rmrypv","bxjxpfp","amarxpg","dmhuq","sviavwoxss","bwowfvira","zfkgsudxq","wnfbo","rxgw","jxkvrmajri","cub","abxvhyehv","bwowfvira","indbvb","ehd","ckqqibnx","oic","ptk","hnnftqf","ouy","oic","zgsedk","abxvhyehv","ypzfk","ptk","sviavwoxss","rmrypv","oic","ous","abxvhyehv","hnnftqf","hfhlfqzkcn","ledleb","cub","ppn","zddeno","indbvb","oic","jlmetsplg","ouy","bwowfvira","bklij","gucayxp","zfkgsudxq","hfhlfqzkcn","zddeno","ledleb","zfkgsudxq","hnnftqf","bgfvfa","jlmetsplg","indbvb","ehd","wnfbo","hnnftqf","rlmdt","bxlr","indbvb","jdbgvc","jlmetsplg","cub","jlgfgwb","ypzfk","indbvb","dmhuq","jlmetsplg","zgsedk","rmrypv","cub","rxgw","ledleb","rxgw","sviavwoxss","ckqqibnx","hdmvplne","dmhuq","wnfbo","jlmetsplg","bxlr","zfkgsudxq","bxjxpfp","ledleb","indbvb","ckqqibnx","ous","ckqqibnx","cub","ous","abxvhyehv","bxlr","hfhlfqzkcn","hfhlfqzkcn","oic","ten","amarxpg","indbvb","cub","alkq","alkq","sviavwoxss","indbvb","bwowfvira","ledleb"]
k = 41
Solution().topKFrequent(words, k)