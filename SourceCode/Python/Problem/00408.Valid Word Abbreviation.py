'''
Level: Medium  Tag: [String]

Given a non-empty string s and an abbreviation abbr,

return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the string "word".
Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example 1:

Given s = "internationalization", abbr = "i12iz4n":

Return true.


Example 2:

Given s = "apple", abbr = "a2e":

Return false.

'''

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i = 0
        j = 0
        count = 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit() == True:
                if abbr[j] == 0:
                    return False
                else:
                    count = count *10 + int(abbr[j])
            else:
                if count != 0:
                    i += count
                    count = 0
                if word[i] != abbr[j]:
                    return False
            if count == 0:
                i += 1
            j += 1

        return True



s = "internationalization"
abbr = "i12iz4n"

s1 = "apple"
abbr1 = "a2e"
print Solution().validWordAbbreviation(s1, abbr1)
