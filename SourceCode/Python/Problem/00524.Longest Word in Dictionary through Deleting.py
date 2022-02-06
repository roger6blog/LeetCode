'''
Level: Medium

Given a string s and a string array dictionary,

return the longest string in the dictionary that can be formed by deleting some of the given string characters.

If there is more than one possible result, return the longest word with the smallest lexicographical order.

If there is no possible result, return the empty string.



Example 1:

Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
Output: "apple"
Example 2:

Input: s = "abpcplea", dictionary = ["a","b","c"]
Output: "a"


Constraints:

1 <= s.length <= 1000
1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 1000
s and dictionary[i] consist of lowercase English letters.

'''

class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        if len(s) == 0 or len(dictionary) == 0:
            return ""

        org_s = s[:]
        ans = []
        for word in dictionary:
            i = 0
            s = org_s[:]
            for w in word:
                if w in s:
                    if len(s) == 1:
                        continue
                    i = s.index(w) + 1
                    s = s[i:]
                else:
                    break
            else:
                while ans and len(word) > len(ans[-1]):
                    ans.pop()

                if not ans or len(word) == len(ans[-1]):
                    ans.append(word)
                    ans.sort()
        if ans:
            print(ans[0])
            return ans[0]

        return ""


s = "abpcplea"
dictionary = ["ale","apple","monkey","plea"]
assert "apple" == Solution().findLongestWord(s, dictionary)

s = "abpcplea"
dictionary = ["a","b","c"]
assert "a" == Solution().findLongestWord(s, dictionary)

s = "abpcplea"
dictionary = ["ale","apple","monkey","plea", "abpcplaaa","abpcllllll","abccclllpppeeaaaa"]
assert "apple" == Solution().findLongestWord(s, dictionary)

s = "bab"
dictionary = ["ba","ab","a","b"]
assert "ab" == Solution().findLongestWord(s, dictionary)

s = "aewfafwafjlwajflwajflwafj"
dictionary = ["apple","ewaf","awefawfwaf","awef","awefe","ewafeffewafewf"]
assert "ewaf" == Solution().findLongestWord(s, dictionary)