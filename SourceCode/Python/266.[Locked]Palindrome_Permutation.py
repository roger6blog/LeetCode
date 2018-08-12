'''

Given a string,

determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

'''

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mid = len(s) / 2
        if len(s) % 2 == 0:
            i = 0
            mid -= 1
            while mid - i >= 0:
                if s[mid-i] != s[mid+i+1]:
                    return False
                i += 1
        else:
            i = 1
            while mid - i >= 0:
                if s[mid-i] != s[mid+i]:
                    return False
                i += 1
        return True

class Solution2(object):
    # "abb" test case will get wrong answer!!!
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            #d[i] = d.get(i, 0) + 1

        count = 0
        for i in d.values():
            if i % 2 != 0:
                count += 1
            if count > 1: # Only allow one alone char
                return False

        return True


print Solution2().canPermutePalindrome("carrac")
print Solution().canPermutePalindrome("abb")