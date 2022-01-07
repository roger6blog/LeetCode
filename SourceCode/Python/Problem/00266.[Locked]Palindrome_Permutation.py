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


    def canPermutePalindromeSet(self, s):
        """
        :type s: str
        :rtype: bool
        """
        oddChars = set()

        for c in s:
            if c in oddChars:
                oddChars.remove(c)
            else:
                oddChars.add(c)

        return len(oddChars) <= 1


    def canPermutePalindrome_counter(self, s):
        from collections import Counter
        char_count = Counter(s)
        odd_count = 0
        for k, v in char_count.items():
            if v % 2 == 1:
                odd_count += 1

        return odd_count < 1

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


print(Solution().canPermutePalindrome_counter("carrac"))
print(Solution().canPermutePalindrome_counter("abb"))
s = "code"
assert False == Solution().canPermutePalindrome_counter(s)
