'''
Level: Medium

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence,

return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

You may return the answer in any order.



Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

Constraints:

1 <= s.length <= 105
s[i] is either 'A', 'C', 'G', or 'T'.

'''


'''
重點是找出兩個有同樣字母組成的子序列
所以用一個set存曾經看過的字母結構序列
要是有出現看過的字母結構序列在裡面的話
就是重複的

'''

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = []
        repeat = []
        for i in range(len(s)):
            dna = s[i:i+10]
            if dna not in seen:
                seen.append(dna)
            else:
                repeat.append(dna)
        print(list(repeat))
        return list(repeat)

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
assert ['AAAAACCCCC', 'CCCCCAAAAA'] == Solution().findRepeatedDnaSequences(s)