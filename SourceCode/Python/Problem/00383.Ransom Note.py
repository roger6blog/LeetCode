'''
Level: Easy

Given two stings ransomNote and magazine,

return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

'''

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine = list(magazine)

        for i in range(len(ransomNote)):
            if ransomNote[i] not in magazine:
                return False
            magazine.remove(ransomNote[i])

        return True

ransomNote = "a"
magazine = "b"
assert False == Solution().canConstruct(ransomNote, magazine)

ransomNote = "aa"
magazine = "ab"
assert False == Solution().canConstruct(ransomNote, magazine)

ransomNote = "aa"
magazine = "aab"
assert True == Solution().canConstruct(ransomNote, magazine)